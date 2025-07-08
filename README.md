# 🛡️ 30 Days of Ethical Hacking & Networking Tools

**Dự án thực hành xây dựng 30 công cụ nhỏ liên quan đến ethical hacking và mạng máy tính.**  
Mỗi ngày triển khai một tool giúp rèn luyện kỹ năng scripting, networking, bảo mật hệ thống và mô phỏng các kỹ thuật pentest hợp pháp.

---

## 🎯 Mục tiêu

- Xây dựng nền tảng kỹ năng bảo mật và tự động hóa công cụ mạng.
- Hiểu rõ cách thức hoạt động của các kỹ thuật trong ethical hacking.
- Làm quen với các thư viện như: `scapy`, `socket`, `paramiko`, `flask`, `nmap`, `requests`...
- Mô phỏng các hành vi thực tế trong mạng, giám sát, tấn công và phòng thủ.
- Tăng tính kỷ luật, viết mã sạch, có tài liệu và tổ chức dự án tốt.

---

## 📅 Danh sách 30 ngày

### 🔍 Tuần 1: Thăm dò & Giám sát Mạng
| Ngày | Tên Tool                        | Mô tả |
|------|----------------------------------|-------|
| 01   | Multi-thread Port Scanner        | Quét port nhanh trên dải IP |
| 02   | Public IP & ISP Checker          | Kiểm tra IP công cộng & nhà mạng |
| 03   | Subnet Ping Sweep                | Tìm thiết bị sống trong mạng nội bộ |
| 04   | Traceroute Visualizer            | Truy dấu tuyến đường, vẽ sơ đồ |
| 05   | ARP Scanner                      | Phát hiện thiết bị LAN bằng ARP |
| 06   | HTTP Packet Sniffer              | Bắt gói HTTP GET/POST chưa mã hóa |
| 07   | PCAP Analyzer                    | Phân tích file PCAP, trích xuất thông tin |

### 🤖 Tuần 2: Tự động hóa & Xâm nhập Cục bộ
| Ngày | Tên Tool                        | Mô tả |
|------|----------------------------------|-------|
| 08   | MAC Address Changer              | Đổi MAC để vượt lọc hoặc ngụy trang |
| 09   | DHCP Starvation Tool             | Gửi hàng loạt yêu cầu DHCP giả |
| 10   | Email Alert on Suspicious Packet | IDS đơn giản gửi email khi phát hiện gói nguy hiểm |
| 11   | Wi-Fi Scanner (CLI)              | Liệt kê SSID, tín hiệu, bảo mật xung quanh |
| 12   | IP Spoofing Lab Tool             | Tạo gói tin giả IP để kiểm tra phản ứng hệ thống |
| 13   | Reverse Shell Generator          | Sinh lệnh reverse shell cho nhiều nền tảng |
| 14   | Port Knocking Tool               | Mở port SSH khi gõ đúng chuỗi knock |

### 🛠️ Tuần 3: Tấn công và Kiểm thử Web/Dịch vụ
| Ngày | Tên Tool                        | Mô tả |
|------|----------------------------------|-------|
| 15   | SSH Brute-force Tester           | Đoán mật khẩu SSH bằng wordlist |
| 16   | Hash Cracker                     | Crack MD5, SHA1, SHA256 |
| 17   | DNS Spoofing (lab)               | Chuyển hướng domain về IP giả |
| 18   | Simple Web Fuzzer                | Gửi yêu cầu đến các endpoint phổ biến |
| 19   | Directory Brute-force Tool       | Tìm folder ẩn bằng wordlist |
| 20   | XSS Payload Tester               | Inject payload XSS lên form đầu vào |
| 21   | SQL Injection Tester             | Gửi payload SQLi đến các input web |

### 🧰 Tuần 4: Phòng thủ – Giám sát – Điều khiển từ xa
| Ngày | Tên Tool                        | Mô tả |
|------|----------------------------------|-------|
| 22   | Firewall Rule Checker            | Kiểm tra rule iptables/ufw nguy hiểm |
| 23   | Snort Rule Trigger               | Viết rule bắt gói chứa nội dung độc hại |
| 24   | Service Monitor + Telegram Alert | Giám sát port, dịch vụ và cảnh báo |
| 25   | Auto VPN Client Connector        | Kết nối VPN tự động khi boot |
| 26   | Python Keylogger (lab only)      | Ghi log phím bấm – lab/test only |
| 27   | Wi-Fi Deauth Tool (Scapy)        | Ngắt kết nối Wi-Fi client trong lab |
| 28   | Telegram Remote Controller Bot   | Điều khiển từ xa: ping, scan, gửi log |
| 29   | Network Dashboard (Grafana)      | Theo dõi trạng thái mạng qua dashboard |
| 30   | Tổng kết & Đóng gói dự án        | Gom lại toàn bộ tool, viết hướng dẫn |

---

## 🧱 Cấu trúc thư mục

```bash
30days-Ethical-Hacking-and-Networking-tool/
│
├── day01-Multi-thread-Port-Scanner/
├── day02-Public-IP-Checker/
├── ...
├── day30-Project-Summary/
│
├── README.md
└── requirements.txt
## ⚙️ Cài đặt & Chạy thử

### Cài đặt thư viện

```bash
pip install -r requirements.txt
```

### Chạy ví dụ

```bash
cd day01-Multi-thread-Port-Scanner
python3 scanner.py
```

---

## ⚠️ Cảnh báo pháp lý

> **Dự án chỉ dành cho mục đích học tập và mô phỏng trong lab cá nhân.**
> Không sử dụng để tấn công, xâm nhập, giám sát bất kỳ hệ thống nào mà bạn không sở hữu hoặc không có quyền hợp pháp.
> Mọi hành vi sử dụng sai mục đích là trách nhiệm của người dùng – **tôi không chịu trách nhiệm pháp lý cho việc lạm dụng**.

---

## 📫 Liên hệ

* GitHub: [https://github.com/your-username](https://github.com/your-username)
* Email: [your.email@example.com](mailto:your.email@example.com)

---

**📌 Theo dõi repo để cập nhật tool mỗi ngày và cùng mình hoàn thành thử thách nhé!**
