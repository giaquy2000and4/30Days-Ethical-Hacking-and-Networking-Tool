import argparse
import csv
import requests
from scapy.layers.l2 import ARP, Ether
from scapy.sendrecv import srp

def get_mac_vendor(mac_address):
    """Truy vấn vendor từ MAC thông qua API"""
    try:
        url = f"https://api.macvendors.com/{mac_address}"
        response = requests.get(url, timeout=3)
        if response.status_code == 200:
            return response.text
        else:
            return "Unknown"
    except:
        return "Unknown"

def arp_scan(ip_range):
    """Thực hiện ARP scan trong dải IP"""
    arp = ARP(pdst=ip_range)
    ether = Ether(dst="ff:ff:ff:ff:ff:ff")
    packet = ether/arp

    result = srp(packet, timeout=2, verbose=0)[0]

    devices = []
    for sent, received in result:
        mac = received.hwsrc
        ip = received.psrc
        vendor = get_mac_vendor(mac)
        devices.append({'IP': ip, 'MAC': mac, 'Vendor': vendor})

    return devices

def save_to_csv(devices, filename):
    """Lưu danh sách thiết bị ra file CSV"""
    with open(filename, mode='w', newline='') as file:
        writer = csv.DictWriter(file, fieldnames=['IP', 'MAC', 'Vendor'])
        writer.writeheader()
        for dev in devices:
            writer.writerow(dev)

def main():
    parser = argparse.ArgumentParser(description="ARP Scan LAN Tool - by ChatGPT")
    parser.add_argument("-r", "--range", help="Dải IP cần quét (ví dụ: 192.168.1.0/24)", required=True)
    parser.add_argument("-o", "--output", help="Tên file CSV để lưu kết quả (tùy chọn)", default="arp_result.csv")

    args = parser.parse_args()

    print(f"[+] Đang quét dải IP: {args.range}\n")
    devices = arp_scan(args.range)

    print("{:<15} {:<20} {:<}".format("IP Address", "MAC Address", "Vendor"))
    print("-" * 60)
    for dev in devices:
        print("{:<15} {:<20} {:<}".format(dev['IP'], dev['MAC'], dev['Vendor']))

    if args.output:
        save_to_csv(devices, args.output)
        print(f"\n[+] Kết quả đã lưu vào: {args.output}")

if __name__ == "__main__":
    main()
