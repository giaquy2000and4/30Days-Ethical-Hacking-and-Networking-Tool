# ARP Scan Tool

Công cụ quét mạng LAN sử dụng giao thức ARP để phát hiện các thiết bị trong mạng cục bộ.

## Tính năng

- Quét dải IP để phát hiện thiết bị đang hoạt động
- Hiển thị địa chỉ IP, MAC address và thông tin nhà sản xuất
- Lưu kết quả vào file CSV
- Giao diện dòng lệnh đơn giản

## Yêu cầu hệ thống

- Python 3.x
- Quyền administrator/root (cần thiết để gửi ARP packets)

## Cài đặt

1. Cài đặt các thư viện cần thiết:
```bash
pip install scapy requests
```

2. Tải xuống file `arp_scan.py`

## Cách sử dụng

### Cú pháp cơ bản:
```bash
python arp_scan.py -r <dải_IP>
```

### Các tùy chọn:
- `-r, --range`: Dải IP cần quét (bắt buộc)
- `-o, --output`: Tên file CSV để lưu kết quả (tùy chọn, mặc định: arp_result.csv)

### Ví dụ sử dụng:

1. Quét dải IP 192.168.1.0/24:
```bash
python arp_scan.py -r 192.168.1.0/24
```

2. Quét và lưu kết quả vào file tùy chỉnh:
```bash
python arp_scan.py -r 192.168.1.0/24 -o ketqua_quet.csv
```

3. Quét dải IP khác:
```bash
python arp_scan.py -r 10.0.0.0/24
```

## Kết quả đầu ra

Chương trình sẽ hiển thị bảng kết quả với các cột:
- **IP Address**: Địa chỉ IP của thiết bị
- **MAC Address**: Địa chỉ MAC của thiết bị
- **Vendor**: Nhà sản xuất thiết bị (dựa trên MAC address)

Ví dụ:
```
IP Address      MAC Address          Vendor
------------------------------------------------------------
192.168.1.1     aa:bb:cc:dd:ee:ff    TP-Link Technologies Co.,Ltd.
192.168.1.100   11:22:33:44:55:66    Samsung Electronics Co.,Ltd
```

## Lưu ý quan trọng

- **Quyền quản trị**: Cần chạy với quyền administrator (Windows) hoặc root (Linux/Mac) để có thể gửi ARP packets
- **Tường lửa**: Một số tường lửa có thể chặn ARP packets
- **Thời gian quét**: Thời gian quét phụ thuộc vào kích thước dải IP và tốc độ mạng

## Chạy với quyền quản trị

### Windows:
```bash
# Mở Command Prompt với quyền Administrator
python arp_scan.py -r 192.168.1.0/24
```

### Linux/Mac:
```bash
sudo python arp_scan.py -r 192.168.1.0/24
```

## File CSV

Kết quả được lưu trong file CSV với định dạng:
```csv
IP,MAC,Vendor
192.168.1.1,aa:bb:cc:dd:ee:ff,TP-Link Technologies Co.,Ltd.
192.168.1.100,11:22:33:44:55:66,Samsung Electronics Co.,Ltd
```

## Xử lý lỗi thường gặp

1. **Permission denied**: Cần chạy với quyền quản trị
2. **Module not found**: Cài đặt thư viện bằng `pip install scapy requests`
3. **No devices found**: Kiểm tra dải IP có đúng không, hoặc không có thiết bị nào đang hoạt động

## Thông tin bổ sung

- Chương trình sử dụng API từ macvendors.com để tra cứu thông tin nhà sản xuất
- Timeout mặc định cho ARP scan là 2 giây
- Timeout cho API request là 3 giây

## Hỗ trợ

Nếu gặp vấn đề, vui lòng kiểm tra:
- Quyền quản trị
- Kết nối internet (để tra cứu vendor)
- Cài đặt đúng thư viện
- Định dạng dải IP đúng (ví dụ: 192.168.1.0/24)