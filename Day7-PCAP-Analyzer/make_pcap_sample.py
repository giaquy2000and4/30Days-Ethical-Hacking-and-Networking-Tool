from scapy.all import Ether, IP, TCP, UDP, DNS, DNSQR, Raw, wrpcap

packets = []

# DNS Query
dns_pkt = Ether()/IP(src="192.168.0.7", dst="8.8.8.8")/UDP(sport=12345, dport=53)/DNS(rd=1, qd=DNSQR(qname="test.local"))
packets.append(dns_pkt)

# HTTP GET
http_get = (
    "GET / HTTP/1.1\r\n"
    "Host: test.local\r\n"
    "User-Agent: curl/7.68.0\r\n"
    "Accept: */*\r\n\r\n"
)
packets.append(
    Ether()/IP(src="192.168.0.7", dst="192.168.0.8")/TCP(sport=1234, dport=80)/Raw(load=http_get)
)

# HTTP POST (login)
http_post = (
    "POST /login HTTP/1.1\r\n"
    "Host: test.local\r\n"
    "Content-Type: application/x-www-form-urlencoded\r\n"
    "Content-Length: 29\r\n\r\n"
    "username=admin&password=123"
)
packets.append(
    Ether()/IP(src="192.168.0.7", dst="192.168.0.8")/TCP(sport=1235, dport=80)/Raw(load=http_post)
)

# HTTP POST (file upload)
multipart = (
    "POST /upload HTTP/1.1\r\n"
    "Host: test.local\r\n"
    "Content-Type: multipart/form-data; boundary=----WebKitFormBoundary\r\n\r\n"
    "------WebKitFormBoundary\r\n"
    "Content-Disposition: form-data; name=\"file\"; filename=\"test.txt\"\r\n"
    "Content-Type: text/plain\r\n\r\n"
    "This is the content of the uploaded file.\r\n"
    "------WebKitFormBoundary--\r\n"
)
packets.append(
    Ether()/IP(src="192.168.0.7", dst="192.168.0.8")/TCP(sport=1236, dport=80)/Raw(load=multipart)
)

# Ghi ra file .pcap
wrpcap("sample-http-dns.pcap", packets)
print("✅ Đã tạo file sample-http-dns.pcap")
