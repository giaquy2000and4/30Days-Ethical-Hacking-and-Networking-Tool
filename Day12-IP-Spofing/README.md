
````markdown
# 🛠 IP Spoofing & SYN Flood Tools (Scapy)

Công cụ mô phỏng kỹ thuật IP spoofing và SYN Flood dùng thư viện [Scapy](https://scapy.net/) bằng Python. Dùng trong môi trường lab để kiểm tra khả năng chịu tải của thiết bị mạng và hiểu nguyên lý tấn công từ chối dịch vụ (DoS).

---

## 📁 Danh sách file

| Tên file              | Mô tả |
|------------------------|-------|
| `ip_spoof_menu.py`     | Gửi gói ICMP hoặc TCP SYN với IP giả mạo. Có menu tương tác trong terminal. |
| `syn_flood.py`         | Gửi hàng loạt TCP SYN tới máy đích để mô phỏng SYN Flood attack. |

---

## 🧪 Mô hình lab đề xuất

```plaintext
[MÁY TẤN CÔNG] ─LAN─┬────────────┐
                   │            │
               [ROUTER CHÍNH]   │
                   │            │
               [ROUTER PHỤ] ◄───┘ (WAN)
````

* Máy tấn công cắm LAN vào **router chính**
* WAN của **router phụ** kết nối vào router chính
* Gửi SYN flood từ máy tấn công tới IP WAN của router phụ

---

##  Cách sử dụng

### 1. IP Spoofing có menu (`ip_spoof_menu.py`)

```bash
python ip_spoof_menu.py
```

* Chọn chế độ: ICMP hoặc TCP SYN
* Nhập IP đích và IP giả mạo
* Công cụ sẽ gửi 1 gói spoof và hiển thị log

---

### 2. SYN Flood (`syn_flood.py`)

```bash
python syn_flood.py
```

* Nhập IP đích, port, và số gói muốn gửi
* Công cụ sẽ gửi hàng loạt gói TCP SYN với IP ngẫu nhiên (giả mạo)
* Có thể gây lag hoặc treo dịch vụ TCP của máy đích

---

## ️ Cảnh báo

*  **Chỉ dùng trong lab riêng hoặc mạng nội bộ**
*  **Không được sử dụng để tấn công các hệ thống không thuộc quyền sở hữu**
*  Mục đích: giáo dục, nghiên cứu, kiểm tra bảo mật mạng

---

##  Kiểm chứng & quan sát

* Dùng Wireshark để bắt gói tại máy đích hoặc router
* Quan sát trạng thái `SYN_RECV` với `netstat -nat`
* Kiểm tra log hệ thống hoặc web GUI router

---

##  Yêu cầu

* Python 3.x
* Scapy: cài đặt bằng `pip install scapy`
* Chạy với quyền admin hoặc sudo

---

##  License

MIT – Dành cho nghiên cứu và học tập.


