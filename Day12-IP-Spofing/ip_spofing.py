from scapy.layers.inet import IP, ICMP, TCP
from scapy.sendrecv import send
from scapy.volatile import RandShort

def send_icmp(target_ip, spoofed_ip):
    pkt = IP(src=spoofed_ip, dst=target_ip) / ICMP()
    send(pkt, verbose=False)
    print(f"[+] Đã gửi gói ICMP từ {spoofed_ip} đến {target_ip}")

def send_tcp_syn(target_ip, target_port, spoofed_ip):
    pkt = IP(src=spoofed_ip, dst=target_ip) / TCP(sport=RandShort(), dport=target_port, flags="S")
    send(pkt, verbose=False)
    print(f"[+] Đã gửi gói TCP SYN từ {spoofed_ip} đến {target_ip}:{target_port}")

def main_menu():
    print("=== IP Spoofing Tool ===")
    print("1. Gửi ICMP Echo (ping giả mạo IP)")
    print("2. Gửi TCP SYN (kết nối giả mạo IP)")
    print("0. Thoát")

    choice = input("Chọn chế độ (0-2): ").strip()

    if choice == "0":
        print("Thoát chương trình.")
        return

    target_ip = input("Nhập IP đích: ").strip()
    spoofed_ip = input("Nhập IP giả mạo: ").strip()

    if choice == "1":
        send_icmp(target_ip, spoofed_ip)
    elif choice == "2":
        try:
            target_port = int(input("Nhập port đích (mặc định 80): ").strip() or "80")
            send_tcp_syn(target_ip, target_port, spoofed_ip)
        except ValueError:
            print("Port không hợp lệ!")
    else:
        print("Lựa chọn không hợp lệ!")

    print()
    input("Nhấn Enter để tiếp tục...")
    main_menu()

if __name__ == "__main__":
    main_menu()
