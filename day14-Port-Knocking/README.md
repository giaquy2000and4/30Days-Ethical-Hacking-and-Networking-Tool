# 🔐 Hệ thống Port Knocking trên WSL

Hướng dẫn đầy đủ để cài đặt và cấu hình hệ thống Port Knocking bảo mật cho SSH trên Windows Subsystem for Linux (WSL).

## 📖 Tổng quan

Port Knocking là một kỹ thuật bảo mật mạng cho phép ẩn các dịch vụ (như SSH) khỏi những kẻ tấn công. Hệ thống sẽ:

- **Chặn SSH (port 22)** theo mặc định bằng `iptables`
- **Mở SSH tạm thời** khi client gõ đúng chuỗi port (port knocking)
- Tự động khởi động `ssh` và `knockd` mỗi khi khởi động WSL
- Sử dụng **Windows làm client** và **WSL làm server**

## 🛠️ Yêu cầu hệ thống

### Trên WSL (Ubuntu):
- SSH server (`openssh-server`)
- Knock daemon (`knockd`)
- `iptables`

### Trên Windows:
- Công cụ gửi port knock (`nmap` hoặc Python)

## 🚀 Cài đặt và cấu hình

### Bước 1: Cài đặt các gói cần thiết

```bash
sudo apt update
sudo apt install knockd iptables openssh-server -y
```

### Bước 2: Cấu hình knockd

Chỉnh sửa file cấu hình knockd:

```bash
sudo nano /etc/knockd.conf
```

Dán nội dung sau (có thể thay đổi các port):

```ini
[options]
    logfile = /var/log/knockd.log
    interface = eth0

[openSSH]
    sequence = 1234,5678,9012
    seq_timeout = 15
    command = /sbin/iptables -A INPUT -s %IP% -p tcp --dport 22 -j ACCEPT
    tcpflags = syn

[closeSSH]
    sequence = 9012,5678,1234
    seq_timeout = 15
    command = /sbin/iptables -D INPUT -s %IP% -p tcp --dport 22 -j ACCEPT
    tcpflags = syn
```

> 💡 **Lưu ý:** Bạn có thể sử dụng bất kỳ số port nào trong chuỗi.

### Bước 3: Chặn SSH theo mặc định

```bash
sudo iptables -A INPUT -p tcp --dport 22 -j DROP
```

### Bước 4: Thiết lập tự động khởi động

Tạo script khởi động:

```bash
nano ~/.start_knockd.sh
```

Dán nội dung:

```bash
#!/bin/bash

echo "[+] Starting SSH service..."
sudo service ssh start

echo "[+] Starting knockd..."
sudo knockd -d &
```

Cấp quyền thực thi:

```bash
chmod +x ~/.start_knockd.sh
```

Chỉnh sửa `~/.bashrc` để chạy tự động:

```bash
nano ~/.bashrc
```

Thêm vào cuối file:

```bash
bash ~/.start_knockd.sh
```

## 🔑 Sử dụng Port Knocking từ Windows

### Phương pháp 1: Sử dụng `nmap`

Mở **CMD/PowerShell** và chạy:

```bash
nmap -Pn -p 1234 <WSL_IP>
nmap -Pn -p 5678 <WSL_IP>
nmap -Pn -p 9012 <WSL_IP>
```

> Thay `<WSL_IP>` bằng địa chỉ IP của WSL. Lấy IP bằng lệnh:

```bash
ip addr | grep eth0
```

hoặc:

```bash
ip route
```

Tìm địa chỉ có dạng `172.27.x.x`.

### Phương pháp 2: Sử dụng Python

Tạo file `knock.py` trên Windows:

```python
import socket
import time

target_ip = "172.27.199.168"  # Thay bằng IP WSL của bạn
ports = [1234, 5678, 9012]     # Thay bằng chuỗi port của bạn

for port in ports:
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(0.5)
        sock.connect((target_ip, port))
        sock.close()
    except:
        pass
    time.sleep(1)

print("Hoàn thành port knocking.")
```

Chạy script:

```bash
python knock.py
```

## 🧪 Kiểm tra kết nối SSH

Sau khi thực hiện port knocking, kết nối SSH từ Windows:

```bash
ssh username@172.27.199.168
```

> Thay `username` bằng tên người dùng WSL của bạn.

Nếu thành công, bạn sẽ đăng nhập vào WSL.

## 📊 Kiểm tra logs và debug

Xem hoạt động của `knockd`:

```bash
tail -f /var/log/knockd.log
```

Ví dụ log khi knock thành công:

```
[2025-07-21 22:27] 172.27.192.1: openSSH: Stage 1
[2025-07-21 22:27] 172.27.192.1: openSSH: Stage 2
[2025-07-21 22:27] 172.27.192.1: openSSH: Stage 3
```

Kiểm tra quy tắc iptables:

```bash
sudo iptables -L -n | grep 22
```

Sẽ hiển thị quy tắc cho phép SSH từ IP của bạn.

## 🔒 Đóng kết nối SSH

### Tự động đóng theo thời gian

Thêm cron job để chạy lệnh:

```bash
sudo iptables -D INPUT -p tcp --dport 22 -s YOUR_IP -j ACCEPT
```

### Đóng bằng port knocking

Knock chuỗi `closeSSH`:

```bash
nmap -Pn -p 9012 <WSL_IP>
nmap -Pn -p 5678 <WSL_IP>
nmap -Pn -p 1234 <WSL_IP>
```

## 🔄 Reset cấu hình (khi gặp lỗi)

Xóa tất cả quy tắc iptables:

```bash
sudo iptables -F
```

Thêm lại quy tắc chặn SSH:

```bash
sudo iptables -A INPUT -p tcp --dport 22 -j DROP
```

## 🔧 Tùy chỉnh

### Thay đổi chuỗi port

Chỉnh sửa file `/etc/knockd.conf` và thay đổi:
- `sequence = 1234,5678,9012` thành chuỗi port mong muốn
- Cập nhật script Python hoặc lệnh nmap tương ứng

### Thay đổi thời gian timeout

Điều chỉnh `seq_timeout = 15` trong file cấu hình (đơn vị: giây).

### Sử dụng giao diện mạng khác

Thay đổi `interface = eth0` thành giao diện mạng phù hợp.

## ⚠️ Lưu ý bảo mật

1. **Không chia sẻ chuỗi port** với người khác
2. **Sử dụng chuỗi port phức tạp** và khó đoán
3. **Thay đổi chuỗi định kỳ** để tăng bảo mật
4. **Kiểm tra logs thường xuyên** để phát hiện hoạt động bất thường
5. **Sử dụng SSH key** thay vì mật khẩu để tăng cường bảo mật

## 🎯 Kết luận

Port Knocking là một lớp bảo mật bổ sung hiệu quả, giúp ẩn dịch vụ SSH khỏi các cuộc tấn công brute force và port scanning. Kết hợp với các biện pháp bảo mật khác như SSH key authentication, fail2ban, và cấu hình SSH an toàn sẽ tạo ra một hệ thống bảo mật mạnh mẽ.

---

**Tác giả:** [Tên của bạn]  
**Phiên bản:** 1.0  
**Cập nhật lần cuối:** 21/07/2025