# PCAP Analyzer

Công cụ phân tích gói tin mạng (PCAP) sử dụng Python và Scapy để tạo và phân tích các gói tin HTTP, DNS.

## Tổng quan

Dự án này bao gồm hai script chính:
- `make_pcap_sample.py`: Tạo file PCAP mẫu với các gói tin DNS và HTTP
- `pcap_analyzer.py`: Phân tích file PCAP và trích xuất thông tin DNS queries và HTTP requests

## Yêu cầu hệ thống

- Python 3.x
- Thư viện Scapy

## Cài đặt

1. Cài đặt Python 3.x từ [python.org](https://python.org)

2. Cài đặt thư viện Scapy:
```bash
pip install scapy
```

## Sử dụng

### 1. Tạo file PCAP mẫu

Chạy script để tạo file PCAP mẫu:

```bash
python make_pcap_sample.py
```

Script sẽ tạo file `sample-http-dns.pcap` chứa các gói tin mẫu:
- DNS Query đến 8.8.8.8 cho domain `test.local`
- HTTP GET request
- HTTP POST request (đăng nhập với username/password)
- HTTP POST request (upload file)

### 2. Phân tích file PCAP

Chạy script phân tích:

```bash
python pcap_analyzer.py
```

Script sẽ đọc file `sample-http-dns.pcap` và hiển thị:
- Tổng số DNS queries và chi tiết từng query
- Tổng số HTTP requests và chi tiết từng request
- Thông tin POST data nếu chứa username/password
- Thông báo nếu có file upload

## Kết quả mẫu

```
📌 Tổng DNS Query: 1
[DNS] 192.168.0.7 → 8.8.8.8 | Query: test.local.

📌 Tổng HTTP Request: 3
[HTTP] GET http://test.local/ | 192.168.0.7 → 192.168.0.8
--------------------------------------------------------------------------------
[HTTP] POST http://test.local/login | 192.168.0.7 → 192.168.0.8
    🔐 POST data: username=admin&password=123
--------------------------------------------------------------------------------
[HTTP] POST http://test.local/upload | 192.168.0.7 → 192.168.0.8
    📤 Có file upload trong POST body.
--------------------------------------------------------------------------------
```

## Tính năng

### make_pcap_sample.py
- Tạo gói tin DNS query sử dụng UDP
- Tạo HTTP GET request
- Tạo HTTP POST request với form data
- Tạo HTTP POST request với multipart form data (file upload)
- Xuất ra file PCAP có thể mở bằng Wireshark

### pcap_analyzer.py
- Đọc và phân tích file PCAP
- Trích xuất DNS queries với domain name
- Trích xuất HTTP requests (GET/POST)
- Hiển thị thông tin POST data (đặc biệt chú ý username/password)
- Phát hiện file upload trong multipart form data
- Xử lý lỗi để tránh crash khi gặp gói tin không hợp lệ

## Cấu trúc gói tin

### DNS Query
- Source: 192.168.0.7:12345
- Destination: 8.8.8.8:53
- Query: test.local

### HTTP Requests
- Source: 192.168.0.7 (các port khác nhau)
- Destination: 192.168.0.8:80
- Host: test.local

## Lưu ý bảo mật

- File PCAP mẫu chứa thông tin đăng nhập giả (admin/123)
- Chỉ sử dụng cho mục đích học tập và thử nghiệm
- Không sử dụng trên dữ liệu thực tế có thông tin nhạy cảm

## Mở rộng

Bạn có thể mở rộng công cụ này để:
- Phân tích thêm các giao thức khác (HTTPS, FTP, SSH...)
- Thêm filter theo IP, port, hoặc protocol
- Xuất kết quả ra file JSON/CSV
- Thêm GUI interface
- Phát hiện các pattern bất thường

## Tác giả

Dự án được tạo để học tập và nghiên cứu về network packet analysis.