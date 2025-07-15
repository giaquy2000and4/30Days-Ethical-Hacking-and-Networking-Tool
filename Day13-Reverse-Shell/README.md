
#  Reverse Shell Demo (Python)

Đây là một mô phỏng đơn giản về reverse shell viết bằng Python, giúp bạn hiểu cách hoạt động của tấn công reverse shell giữa attacker và victim trên cùng một máy (localhost) hoặc trong môi trường lab ảo.

---

##  Cấu trúc dự án

```
.
├── listener.py         # Máy attacker: lắng nghe kết nối
└── reverse_shell.py    # Máy victim: gửi kết nối reverse shell
```

---

##  Cách hoạt động

### 1. `listener.py` – **Attacker**
- Chạy trước để mở port (`4444`) và lắng nghe kết nối từ victim.
- Nhận lệnh từ người dùng (`input()`), gửi qua socket tới victim.
- In kết quả trả về.

### 2. `reverse_shell.py` – **Victim**
- Mô phỏng máy bị khai thác, chủ động kết nối TCP tới attacker (`127.0.0.1:4444`).
- Nhận lệnh từ socket, thực thi bằng `subprocess`, và gửi kết quả về lại.

---

##  Cách chạy (trong PyCharm hoặc terminal)

### Bước 1: Mở terminal 1 – chạy listener
```bash
python listener.py
```

### Bước 2: Mở terminal 2 – chạy reverse shell
```bash
python reverse_shell.py
```

> Bạn sẽ thấy shell tương tác từ attacker:
```bash
Shell> whoami
your-username
Shell> dir
...
```

---

## 💡 Ghi chú

- Đây là mô phỏng an toàn chạy trong `localhost`, không gửi dữ liệu ra ngoài internet.
- Mục đích: học tập và hiểu rõ cơ chế reverse shell.
- Bạn có thể thay `127.0.0.1` bằng IP thật nếu chạy trên 2 máy trong cùng mạng LAN.

---

## ⚠️ CẢNH BÁO

❌ Không sử dụng code này ngoài phạm vi thử nghiệm/lab.  
✅ Chỉ dùng cho mục đích học tập, nghiên cứu bảo mật, và kiểm thử an toàn.

---

## 📚 Tài liệu tham khảo

- [OWASP - Reverse Shell](https://owasp.org/www-community/attacks/Reverse_Shell)
- [PayloadsAllTheThings - Reverse Shell Cheatsheet](https://github.com/swisskyrepo/PayloadsAllTheThings/tree/master/Methodology%20and%20Resources/Reverse%20Shell%20Cheatsheet)
