from scapy.all import rdpcap, IP, TCP, Raw, DNS, DNSQR

PCAP_FILE = "sample-http-dns.pcap"
packets = rdpcap(PCAP_FILE)

dns_queries = []
http_requests = []

for pkt in packets:
    # DNS Query
    if pkt.haslayer(DNS) and pkt.haslayer(DNSQR):
        try:
            query = pkt[DNSQR].qname.decode()
            dns_queries.append({
                'src': pkt[IP].src,
                'dst': pkt[IP].dst,
                'query': query
            })
        except:
            pass

    # HTTP GET/POST
    elif pkt.haslayer(TCP) and pkt.haslayer(Raw):
        try:
            payload = pkt[Raw].load.decode(errors="ignore")
            if payload.startswith("GET") or payload.startswith("POST"):
                method = payload.split()[0]
                path = payload.split()[1]
                host = ""
                for line in payload.split("\r\n"):
                    if line.lower().startswith("host:"):
                        host = line.split(": ")[1]
                        break
                headers = payload.split("\r\n\r\n")[0]
                body = payload.split("\r\n\r\n")[1] if "\r\n\r\n" in payload else ""

                http_requests.append({
                    'src': pkt[IP].src,
                    'dst': pkt[IP].dst,
                    'method': method,
                    'path': path,
                    'host': host,
                    'headers': headers,
                    'body': body.strip()
                })
        except:
            pass

# In kết quả
print(f"📌 Tổng DNS Query: {len(dns_queries)}")
for d in dns_queries:
    print(f"[DNS] {d['src']} → {d['dst']} | Query: {d['query']}")

print(f"\n📌 Tổng HTTP Request: {len(http_requests)}")
for h in http_requests:
    print(f"[HTTP] {h['method']} http://{h['host']}{h['path']} | {h['src']} → {h['dst']}")
    if h['method'] == "POST" and ("username" in h['body'] or "password" in h['body']):
        print(f"    🔐 POST data: {h['body']}")
    if "multipart/form-data" in h['headers']:
        print(f"    📤 Có file upload trong POST body.")
    print("-" * 80)
