# Network IDS - Hệ thống Phát hiện Xâm nhập Mạng

## 🔍 Mô tả
Network IDS là một hệ thống giám sát mạng real-time được viết bằng Python, sử dụng Scapy để phát hiện các gói tin đáng ngờ chứa từ khóa bảo mật như "admin", "root", "password". Khi phát hiện, hệ thống sẽ gửi cảnh báo qua email.

## 🚀 Tính năng
- ✅ Giám sát mạng real-time
- ✅ Phát hiện từ khóa bảo mật nguy hiểm
- ✅ Gửi cảnh báo qua email tự động
- ✅ Giao diện console thân thiện
- ✅ Hỗ trợ nhiều network interface

## 📋 Yêu cầu hệ thống
- Python 3.7+
- Scapy
- Quyền Administrator/Root (để capture gói tin)

## 🛠️ Cài đặt

### 1. Cài đặt dependencies
```bash
pip install scapy
```

### 2. Cấu hình email
Mở file `network_ids.py` và cập nhật thông tin email:

```python
EMAIL_FROM = "your_email@gmail.com"
EMAIL_TO = ["recipient@gmail.com"]
EMAIL_USER = "your_email@gmail.com"
EMAIL_PASS = "your_app_password"  # Sử dụng App Password cho Gmail
```

**Lưu ý:** Để sử dụng Gmail, bạn cần:
1. Bật 2-Factor Authentication
2. Tạo App Password tại: https://myaccount.google.com/apppasswords
3. Sử dụng App Password thay vì mật khẩu thường

## 🏃‍♂️ Chạy chương trình

### Windows:
```cmd
# Chạy với quyền Administrator
python network_ids.py
```

### Linux/macOS:
```bash
# Chạy với quyền root
sudo python3 network_ids.py
```

## 🧪 Kiểm tra và Test

### 1. Khởi động HTTP Server
Sử dụng HTTP server có sẵn của Python:

```bash
# Chạy HTTP server trên port 80 (cần quyền admin/root)
python -m http.server 80

# Hoặc chạy trên port 8080 (không cần quyền admin)
python -m http.server 8080
```

**Lưu ý:** 
- Port 80 cần quyền Administrator/root
- Port 8080 có thể chạy với user thường

### 2. Gửi gói tin test với curl
Sử dụng curl để gửi HTTP requests chứa từ khóa nguy hiểm:

```bash
# Test với từ khóa "admin" trong User-Agent
curl -H "User-Agent: admin" http://localhost:8080/

# Test với từ khóa "password" trong header
curl -H "X-Password: password123" http://localhost:8080/

# Test với từ khóa "root" trong URL
curl "http://localhost:8080/?user=root"

# Test với POST data chứa từ khóa
curl -X POST -d "username=admin&password=secret" http://localhost:8080/login

# Test bình thường (không trigger alert)
curl http://localhost:8080/
```

### 3. Hoặc sử dụng Python script
Tạo file `send_test_packets.py`:

```python
import requests
import time

def send_test_requests(base_url='http://localhost:8080'):
    test_cases = [
        # Test với User-Agent header
        {'method': 'GET', 'url': base_url, 'headers': {'User-Agent': 'admin'}},
        
        # Test với custom header
        {'method': 'GET', 'url': base_url, 'headers': {'X-Auth': 'root'}},
        
        # Test với POST data
        {'method': 'POST', 'url': base_url, 'data': {'username': 'admin', 'password': 'secret'}},
        
        # Test với query parameters
        {'method': 'GET', 'url': f'{base_url}/?user=passwd'},
        
        # Test bình thường
        {'method': 'GET', 'url': base_url},
    ]
    
    for i, test_case in enumerate(test_cases, 1):
        try:
            print(f"[*] Test {i}: {test_case['method']} request...")
            
            if test_case['method'] == 'GET':
                response = requests.get(
                    test_case['url'], 
                    headers=test_case.get('headers', {}),
                    timeout=5
                )
            else:
                response = requests.post(
                    test_case['url'], 
                    data=test_case.get('data', {}),
                    headers=test_case.get('headers', {}),
                    timeout=5
                )
            
            print(f"[+] Response: {response.status_code}")
            
        except Exception as e:
            print(f"[!] Lỗi: {e}")
        
        time.sleep(2)  # Đợi 2 giây giữa các request

if __name__ == "__main__":
    print("[*] Bắt đầu gửi Insta-Hunter-Img requests...")
    send_test_requests()
    print("[*] Hoàn thành Insta-Hunter-Img!")
```

**Cài đặt requests nếu chưa có:**
```bash
pip install requests
```

### 4. Chạy test
```bash
# Chạy Python script
python send_test_packets.py

# Hoặc sử dụng curl commands ở trên
```

## 📊 Quy trình Test đầy đủ

### Bước 1: Chuẩn bị
1. Mở 3 terminal/cmd
2. Cấu hình email trong `network_ids.py`

### Bước 2: Khởi động các thành phần
```bash
# Terminal 1: Chạy IDS (với quyền admin/root)
python network_ids.py

# Terminal 2: Chạy HTTP server
python -m http.server 8080

# Terminal 3: Gửi Insta-Hunter-Img requests
curl -H "User-Agent: admin" http://localhost:8080/
# hoặc
python send_test_packets.py
```

### Bước 3: Quan sát kết quả
- **Terminal 1 (IDS)**: Sẽ hiển thị cảnh báo khi phát hiện từ khóa
- **Email**: Nhận cảnh báo về các gói tin đáng ngờ
- **Terminal 2 (HTTP Server)**: Hiển thị các HTTP requests nhận được

## 🔧 Tùy chỉnh

### Thêm từ khóa mới
```python
KEYWORDS = [b"admin", b"root", b"passwd", b"password", b"secret", b"token"]
```

### Thay đổi cấu hình email
```python
EMAIL_FROM = "your_email@gmail.com"
EMAIL_TO = ["admin@company.com", "security@company.com"]
EMAIL_SUBJECT = "🚨 Security Alert - Suspicious Network Activity"
```

## 🐛 Troubleshooting

### Lỗi thường gặp:

1. **"Permission denied"**
   - Chạy với quyền Administrator (Windows) hoặc sudo (Linux/macOS)

2. **"No module named 'scapy'"**
   ```bash
   pip install scapy
   ```

3. **"Authentication failed" (Email)**
   - Kiểm tra App Password Gmail
   - Đảm bảo 2FA đã được bật

4. **Không bắt được gói tin**
   - Kiểm tra interface đã chọn đúng chưa
   - Đảm bảo có traffic trên interface đó

## 🔒 Bảo mật
- Không commit file chứa password/email vào git
- Sử dụng App Password thay vì mật khẩu chính
- Chạy với quyền tối thiểu cần thiết
- Cân nhắc mã hóa thông tin nhạy cảm

## 📝 Log và Monitoring
Để ghi log chi tiết hơn, có thể thêm:

```python
import logging

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler('ids.log'),
        logging.StreamHandler()
    ]
)
```

## 🤝 Đóng góp
Mọi đóng góp và báo lỗi đều được hoan nghênh! Vui lòng tạo issue hoặc pull request.

## 📄 License
MIT License - Xem file LICENSE để biết thêm chi tiết.