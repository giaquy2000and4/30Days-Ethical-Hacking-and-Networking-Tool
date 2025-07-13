#  Thử Thách 30 Ngày: Xây Dựng Công Cụ Ethical Hacking & Mạng

> **⚠️ TUYÊN BỐ PHÁP LÝ**: Tất cả các công cụ và kỹ thuật trong repository này chỉ dành cho mục đích giáo dục. Chỉ sử dụng trên các hệ thống bạn sở hữu hoặc có quyền kiểm thử rõ ràng. Truy cập trái phép vào hệ thống máy tính là bất hợp pháp và phi đạo đức.

##  Tổng Quan Thử Thách

Đây là thử thách 30 ngày, mỗi ngày bạn sẽ xây dựng một công cụ ethical hacking hoặc mạng nhỏ. Tập trung vào **triển khai thực tế**, **ứng dụng thực tế**, và **mô phỏng** các tình huống bảo mật trong môi trường được kiểm soát.

##  Cấu Trúc Dự Án

```
30-day-ethical-hacking-tools/
├── tuan1-tham-do/
│   ├── Day1-Port-Scanner/
│   ├── Day2-ISP-Locator/
│   ├── Day3-Ping-Sweep/
│   ├── Day4-Trace-Route/
│   ├── Day5-ARP-Scan/
│   ├── Day6-HTTP-Capture/
│   └── Day7-PCAP-Analyzer/
├── tuan2-tu-dong-hoa/
│   ├── Day8-MAC-Changer/
│   ├── Day9-DCHP-Starvation/
│   ├── Day10-Netword-IDS + Email-Alert/
│   ├── Day11-Wifi-Scanner/
│   ├── Day12-IP-Spofing/
│   ├── Day13-Reverse-Shell/
│   └── Day14-Port-Knocking/
├── tuan3-tan-cong/
│   ├── ngay15-tan-cong-ssh/
│   ├── ngay16-crack-password/
│   ├── ngay17-gia-mao-dns/
│   ├── ngay18-fuzzer-web/
│   ├── ngay19-quet-thu-muc/
│   ├── ngay20-test-xss/
│   └── ngay21-test-sql/
├── tuan4-phong-thu/
│   ├── ngay22-kiem-tra-firewall/
│   ├── ngay23-quy-tac-ids/
│   ├── ngay24-giam-sat-dich-vu/
│   ├── ngay25-auto-vpn/
│   ├── ngay26-keylogger/
│   ├── ngay27-wifi-deauth/
│   ├── ngay28-bot-telegram/
│   ├── ngay29-dashboard/
│   └── ngay30-hoan-thien/
├── requirements.txt
├── setup.sh
└── README.md
```

##  Phân Chia Theo Tuần

### Tuần 1: Thăm Dò & Giám Sát Mạng
**Ngày 1-7**: Xây dựng công cụ khám phá mạng và thu thập thông tin thụ động

- **Ngày 1**: Port Scanner Đa Luồng
- **Ngày 2**: Tra Cứu IP Công Cộng + ISP
- **Ngày 3**: Quét Ping Subnet
- **Ngày 4**: Traceroute Tùy Chỉnh + Vẽ Đường Đi
- **Ngày 5**: Quét ARP + Phân Tích Thiết Bị LAN
- **Ngày 6**: Sniffer HTTP với Scapy
- **Ngày 7**: Công Cụ Phân Tích PCAP

### Tuần 2: Tự Động Hóa & Xâm Nhập Nội Bộ
**Ngày 8-14**: Tạo công cụ tự động hóa mạng và kiểm thử nội bộ

- **Ngày 8**: Công Cụ Đổi Địa Chỉ MAC
- **Ngày 9**: Công Cụ Tấn Công DHCP Starvation
- **Ngày 10**: IDS Cơ Bản với Cảnh Báo Email
- **Ngày 11**: Máy Quét Wi-Fi CLI
- **Ngày 12**: Công Cụ Giả Mạo IP (Lab)
- **Ngày 13**: Trình Tạo Reverse Shell
- **Ngày 14**: Công Cụ Port Knocking

### Tuần 3: Tấn Công & Phòng Thủ Dịch Vụ
**Ngày 15-21**: Phát triển công cụ bảo mật tấn công cho kiểm thử có kiểm soát

- **Ngày 15**: Brute-force SSH với Paramiko
- **Ngày 16**: Crack Hash Mật Khẩu
- **Ngày 17**: Công Cụ Giả Mạo DNS
- **Ngày 18**: Web Fuzzer Đơn Giản
- **Ngày 19**: Công Cụ Brute-force Thư Mục
- **Ngày 20**: Tester XSS Payload
- **Ngày 21**: Tester SQL Injection

### Tuần 4: Phát Hiện, Bảo Vệ & Dashboard
**Ngày 22-30**: Xây dựng công cụ phòng thủ và hệ thống giám sát

- **Ngày 22**: Kiểm Tra Quy Tắc Firewall
- **Ngày 23**: Quy Tắc IDS Đơn Giản với Snort
- **Ngày 24**: Giám Sát Dịch Vụ với Cảnh Báo Telegram
- **Ngày 25**: Công Cụ Kết Nối VPN Tự Động
- **Ngày 26**: Keylogger Giáo Dục
- **Ngày 27**: Công Cụ Wi-Fi Deauth
- **Ngày 28**: Bot Telegram Điều Khiển Từ Xa
- **Ngày 29**: Dashboard Giám Sát Mạng
- **Ngày 30**: Hoàn Thiện Dự Án Cuối Cùng

## 🛠️ Yêu Cầu Tiên Quyết

### Kiến Thức Cần Có
- Lập trình Python (trình độ trung bình)
- Khái niệm mạng cơ bản (TCP/IP, mô hình OSI)
- Quen thuộc với dòng lệnh Linux
- Hiểu biết về các nguyên tắc cơ bản của cybersecurity

### Yêu Cầu Phần Mềm
- Python 3.8+
- Linux/macOS (khuyến nghị) hoặc Windows với WSL
- Máy ảo để kiểm thử (VirtualBox/VMware)
- Wireshark để phân tích gói tin
- Git để quản lý phiên bản

### Thư Viện Python
```bash
pip install scapy paramiko requests python-telegram-bot
pip install matplotlib graphviz influxdb-client
pip install hashlib threading socket subprocess
```

##  Bắt Đầu

### 1. Clone Repository
```bash
git clone https://github.com/yourusername/30-day-ethical-hacking-tools.git
cd 30-day-ethical-hacking-tools
```

### 2. Thiết Lập Môi Trường
```bash
chmod +x setup.sh
./setup.sh
```

### 3. Tạo Môi Trường Lab
- Thiết lập máy ảo riêng biệt để kiểm thử
- Cấu hình đoạn mạng riêng cho thử nghiệm
- Cài đặt ứng dụng có lỗ hổng (DVWA, bWAPP) để kiểm thử web

### 4. Bắt Đầu Ngày 1
```bash
cd tuan1-tham-do/ngay01-quet-cong
python port_scanner.py --help
```

## 📋 Quy Trình Hàng Ngày

Mỗi ngày theo cấu trúc này:

1. ** Học**: Hiểu mục đích và lý thuyết của công cụ
2. ** Xây Dựng**: Triển khai công cụ với code sạch, có tài liệu
3. ** Kiểm Thử**: Xác minh chức năng trong môi trường kiểm soát
4. ** Tài Liệu**: Viết hướng dẫn sử dụng và bài học rút ra
5. ** Cải Thiện**: Tái cấu trúc và tối ưu hóa code

##  Mục Tiêu Học Tập

Hoàn thành thử thách này, bạn sẽ:
- Hiểu các công cụ và kỹ thuật bảo mật mạng phổ biến
- Có kinh nghiệm thực hành với các thư viện bảo mật Python
- Học cách triển khai các biện pháp bảo mật tấn công và phòng thủ
- Phát triển kỹ năng phân tích và giám sát mạng
- Xây dựng portfolio các công cụ cybersecurity thực tế

##  Hướng Dẫn Đạo Đức

### NÊN LÀM:
- ✅ Chỉ sử dụng công cụ trên hệ thống của bạn hoặc có quyền rõ ràng
- ✅ Kiểm thử trong môi trường lab riêng biệt
- ✅ Tuân thủ tiết lộ có trách nhiệm cho bất kỳ lỗ hổng nào được tìm thấy
- ✅ Sử dụng kiến thức để cải thiện tình trạng bảo mật
- ✅ Chia sẻ nội dung giáo dục với tuyên bố phù hợp

### KHÔNG NÊN LÀM:
- ❌ Kiểm thử trên hệ thống không có ủy quyền
- ❌ Sử dụng công cụ cho mục đích độc hại
- ❌ Bỏ qua ranh giới pháp lý và đạo đức
- ❌ Phân phối công cụ mà không có cảnh báo phù hợp
- ❌ Tham gia vào các hoạt động bất hợp pháp

## 🏆 Tiêu Chí Hoàn Thành

Để hoàn thành thành công thử thách:
- [ ] Xây dựng tất cả 30 công cụ với code hoạt động
- [ ] Kiểm thử mỗi công cụ trong môi trường lab phù hợp
- [ ] Tài liệu hóa việc sử dụng và bài học rút ra
- [ ] Tạo showcase dự án cuối cùng
- [ ] Chia sẻ kiến thức một cách có trách nhiệm

## 📚 Tài Nguyên

### Tài Liệu
- [Tài Liệu Scapy](https://scapy.readthedocs.io/)
- [Tài Liệu Paramiko](https://docs.paramiko.org/)
- [Hướng Dẫn Kiểm Thử OWASP](https://owasp.org/www-project-web-security-testing-guide/)

### Tài Liệu Học Tập
- [Cybrary](https://www.cybrary.it/)
- [SANS Reading Room](https://www.sans.org/reading-room/)
- [Tài Liệu Kali Linux](https://www.kali.org/docs/)

### Môi Trường Lab
- [VulnHub](https://www.vulnhub.com/)
- [HackTheBox](https://www.hackthebox.com/)
- [DVWA](https://github.com/digininja/DVWA)

## 🤝 Đóng Góp

1. Fork repository
2. Tạo feature branch của bạn (`git checkout -b feature/ngay-xx-cong-cu`)
3. Commit thay đổi (`git commit -m 'Thêm Ngày XX: Tên Công Cụ'`)
4. Push lên branch (`git push origin feature/ngay-xx-cong-cu`)
5. Mở Pull Request

## 📄 Giấy Phép

Dự án này được cấp phép theo Giấy phép MIT - xem file [LICENSE](LICENSE) để biết chi tiết.

##  Thông Báo Pháp Lý

Các công cụ và kỹ thuật được trình bày trong repository này chỉ dành cho mục đích giáo dục và kiểm thử được ủy quyền. Các tác giả và người đóng góp không chịu trách nhiệm cho bất kỳ việc sử dụng sai mục đích nào của các công cụ này. Người dùng hoàn toàn chịu trách nhiệm đảm bảo họ có ủy quyền phù hợp trước khi kiểm thử bất kỳ hệ thống nào.

## 🎖️ Lời Cảm Ơn

- Cộng đồng OWASP cho các tài nguyên bảo mật
- Các nhà phát triển Scapy cho thư viện thao tác gói tin mạnh mẽ
- Cộng đồng cybersecurity cho việc chia sẻ kiến thức
- Tất cả những người đóng góp và kiểm thử dự án này

---

**Bắt đầu hành trình của bạn ngay hôm nay! Bắt đầu với Ngày 1 và xây dựng kỹ năng cybersecurity của bạn từng công cụ một.**

## 📞 Hỗ Trợ

- Tạo issue để báo cáo lỗi hoặc đặt câu hỏi
- Tham gia thảo luận để được hỗ trợ từ cộng đồng
- Theo dõi dự án để nhận cập nhật và công cụ mới

Chúc bạn hacking vui vẻ! 🔒💻
