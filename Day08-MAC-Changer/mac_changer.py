import wmi
import random
import re
import winreg
import time
import os
import ctypes

def get_random_mac():
    # Tạo MAC hợp lệ: Locally Administered + Unicast
    mac = [0x02, random.randint(0x00, 0x7f),
           random.randint(0x00, 0xff),
           random.randint(0x00, 0xff),
           random.randint(0x00, 0xff),
           random.randint(0x00, 0xff)]
    return ''.join(f"{b:02X}" for b in mac)

def list_interfaces():
    c = wmi.WMI()
    interfaces = []
    for nic in c.Win32_NetworkAdapter():
        if (
            nic.PhysicalAdapter
            and nic.MACAddress
            and not any(kw in nic.Name for kw in ["Virtual", "VMware", "Hyper-V", "Wi-Fi Direct", "VPN"])
        ):
            interfaces.append(nic.Name.strip())
    return interfaces

def set_mac_address(interface_name, new_mac):
    reg_path = r'SYSTEM\CurrentControlSet\Control\Class\{4d36e972-e325-11ce-bfc1-08002be10318}'
    try:
        for i in range(1000):
            try:
                key = winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE, f"{reg_path}\\{i:04}", 0, winreg.KEY_ALL_ACCESS)
                try:
                    name, _ = winreg.QueryValueEx(key, "DriverDesc")
                    if name.strip() == interface_name:
                        print(f"[+] Tìm thấy adapter: {name}")
                        winreg.SetValueEx(key, "NetworkAddress", 0, winreg.REG_SZ, new_mac)
                        winreg.CloseKey(key)
                        return True
                except FileNotFoundError:
                    pass
                winreg.CloseKey(key)
            except FileNotFoundError:
                break
    except Exception as e:
        print(f"[!] Lỗi Registry: {e}")
        return False

    print("[!] Không tìm thấy interface.")
    return False

def disable_interface(name):
    c = wmi.WMI()
    for nic in c.Win32_NetworkAdapter():
        if nic.Name.strip() == name:
            result = nic.Disable()
            time.sleep(2)
            return result

def enable_interface(name):
    c = wmi.WMI()
    for nic in c.Win32_NetworkAdapter():
        if nic.Name.strip() == name:
            result = nic.Enable()
            time.sleep(2)
            return result

def restart_adapter(interface_name):
    print("[*] Đang disable interface...")
    disable_interface(interface_name)
    print("[*] Đang enable interface...")
    enable_interface(interface_name)

def get_current_mac(interface_name):
    c = wmi.WMI()
    for nic in c.Win32_NetworkAdapter():
        if nic.Name.strip().lower() == interface_name.lower():
            if nic.MACAddress:
                return nic.MACAddress.replace(":", "").replace("-", "")
    return None

def run_mac_changer():
    print("=== Windows MAC Changer Tool ===\n")

    interfaces = list_interfaces()
    if not interfaces:
        print("[!] Không tìm thấy interface nào phù hợp.")
        return

    print("Danh sách interface khả dụng:")
    for idx, name in enumerate(interfaces):
        print(f"{idx}. {name}")

    try:
        choice = int(input("\nChọn số thứ tự interface bạn muốn thay đổi MAC: "))
        interface_name = interfaces[choice]
    except (ValueError, IndexError):
        print("[!] Lựa chọn không hợp lệ.")
        return

    print(f"[+] Đã chọn: {interface_name}")
    user_mac = input("Nhập MAC mới (hoặc Enter để tạo ngẫu nhiên): ").strip()
    if not user_mac:
        user_mac = get_random_mac()
        print(f"[+] MAC ngẫu nhiên được tạo: {user_mac}")

    old_mac = get_current_mac(interface_name)
    print(f"[+] MAC hiện tại: {old_mac or 'Không xác định'}")

    success = set_mac_address(interface_name, user_mac)
    if success:
        print("[+] Đổi MAC trong registry thành công. Đang khởi động lại interface...")
        restart_adapter(interface_name)
        time.sleep(3)  # Chờ driver cập nhật

        new_mac = get_current_mac(interface_name)
        if new_mac and new_mac.lower() == user_mac.lower():
            print(f"[✓] MAC đã được đổi thành: {new_mac}")
        else:
            print(f"[✗] Không thể xác minh MAC mới. MAC hiện tại: {new_mac or 'Không xác định'}")
    else:
        print("[✗] Thất bại khi thay đổi MAC.")

if __name__ == "__main__":
    if os.name != "nt":
        print("[!] Tool này chỉ hỗ trợ Windows.")
    elif not ctypes.windll.shell32.IsUserAnAdmin():
        print("[!] Vui lòng chạy chương trình với quyền Administrator.")
    else:
        run_mac_changer()
