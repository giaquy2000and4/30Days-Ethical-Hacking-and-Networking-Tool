# HTTP Capture Tool

Công cụ bắt và phân tích gói tin HTTP trên mạng, cho phép theo dõi các yêu cầu HTTP GET và POST đi qua interface mạng.

## Tính năng

- Bắt gói tin HTTP trên port 80
- Phân tích và hiển thị thông tin chi tiết các yêu cầu GET và POST
- Hiển thị URL đầy đủ và payload của POST requests
- Theo dõi real-time các giao tiếp HTTP

## Yêu cầu hệ thống

- Python 3.x
- Quyền administrator/root (cần thiết để bắt gói tin mạng)

## Cài đặt

1. Cài đặt thư viện Scapy:
```bash
pip install scapy
```

2. Tải xuống file `http_capture.py`

## Cách sử dụng

### Chạy chương trình:
```bash
python http_capture.py
```

### Chạy với quyền quản trị:

**Windows:**
```bash
# Mở Command Prompt với quyền Administrator
python http_capture.py
```

**Linux/Mac:**
```bash
sudo python http_capture.py
```

### Dừng chương trình:
Nhấn `Ctrl+C` để dừng việc bắt gói tin

## Kết quả đầu ra

Chương trình sẽ hiển thị thông tin chi tiết về các HTTP requests:

### Ví dụ GET request:
```
[+] GET request from 192.168.1.100 to 93.184.216.34
    URL: http://example.com/index.html
```

### Ví dụ POST request:
```
[+] POST request from 192.168.1.100 to 192.168.1.1
    URL: http://login.example.com/auth
    Payload: username=admin&password=123456
```

## Thông tin hiển thị

Đối với mỗi HTTP request được bắt, chương trình sẽ hiển thị:

- **Phương thức HTTP**: GET hoặc POST
- **IP nguồn**: Địa chỉ IP của máy gửi request
- **IP đích**: Địa chỉ IP của server nhận request
- **URL đầy đủ**: Bao gồm domain và đường dẫn
- **Payload**: Dữ liệu gửi kèm (chỉ với POST requests)

## Lưu ý quan trọng

### Bảo mật và pháp lý
- **Chỉ sử dụng trên mạng của bạn**: Không được sử dụng để theo dõi trái phép
- **Tuân thủ pháp luật**: Đảm bảo có quyền giám sát mạng trước khi sử dụng
- **Bảo vệ dữ liệu**: Các thông tin nhạy cảm có thể được hiển thị (mật khẩu, cookie, v.v.)

### Kỹ thuật
- **Quyền quản trị**: Bắt buộc để có thể bắt gói tin mạng
- **Chỉ HTTP**: Không bắt được HTTPS (port 443) do mã hóa
- **Port 80**: Chỉ giám sát traffic trên port 80 (HTTP tiêu chuẩn)

## Hạn chế

1. **Không hỗ trợ HTTPS**: Do dữ liệu được mã hóa
2. **Chỉ port 80**: Không bắt HTTP trên các port khác
3. **Giao diện mạng**: Chỉ bắt trên interface mạng mặc định
4. **Không lưu trữ**: Dữ liệu chỉ hiển thị real-time, không lưu file

## Mở rộng chức năng

Có thể tùy chỉnh chương trình để:

### Thay đổi port giám sát:
```python
# Thay đổi filter để bắt port khác
sniff(filter="tcp port 8080", prn=http_packet_callback, store=False)
```

### Bắt nhiều port:
```python
# Bắt nhiều port cùng lúc
sniff(filter="tcp port 80 or tcp port 8080", prn=http_packet_callback, store=False)
```

### Lưu vào file:
Có thể mở rộng để lưu các request vào file log hoặc database.

## Xử lý lỗi thường gặp

1. **Permission denied**: 
   - Chạy với quyền administrator/root
   - Kiểm tra quyền truy cập interface mạng

2. **No module named 'scapy'**:
   - Cài đặt: `pip install scapy`

3. **Không bắt được gói tin**:
   - Kiểm tra có traffic HTTP trên port 80
   - Thử truy cập website HTTP (không phải HTTPS)

4. **Decode errors**:
   - Chương trình tự động bỏ qua các gói tin không decode được

## Ứng dụng thực tế

- **Phân tích mạng**: Theo dõi traffic HTTP trong mạng LAN
- **Debug ứng dụng**: Xem các API calls từ ứng dụng web
- **Kiểm tra bảo mật**: Phát hiện truyền dữ liệu không mã hóa
- **Học tập**: Hiểu cách hoạt động của giao thức HTTP

## Cảnh báo bảo mật

⚠️ **Cảnh báo**: Công cụ này có thể thu thập thông tin nhạy cảm như:
- Tên đăng nhập và mật khẩu
- Dữ liệu form
- Session cookies
- Thông tin cá nhân

Chỉ sử dụng trên mạng bạn sở hữu hoặc có quyền giám sát hợp pháp.