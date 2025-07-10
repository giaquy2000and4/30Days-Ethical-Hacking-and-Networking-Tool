from scapy.all import sniff, TCP, Raw, IP

def http_packet_callback(packet):
    if packet.haslayer(TCP) and packet.haslayer(Raw) and packet.haslayer(IP):
        payload = packet[Raw].load
        try:
            data = payload.decode('utf-8')
            if data.startswith("GET") or data.startswith("POST"):
                ip_src = packet[IP].src
                ip_dst = packet[IP].dst

                lines = data.split('\r\n')
                request_line = lines[0]
                method, path, _ = request_line.split()
                host = ''
                for line in lines:
                    if line.lower().startswith("host:"):
                        host = line.split(":", 1)[1].strip()
                        break

                url = f"http://{host}{path}"
                print(f"\n[+] {method} request from {ip_src} to {ip_dst}")
                print(f"    URL: {url}")

                if method == "POST":
                    post_data = lines[-1] if lines[-1] else "<No Payload>"
                    print(f"    Payload: {post_data}")
        except Exception:
            pass  # Ignore decode errors

print("[*] Starting HTTP sniffer... (Press Ctrl+C to stop)\n")
sniff(filter="tcp port 80", prn=http_packet_callback, store=False)
