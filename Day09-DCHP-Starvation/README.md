# DHCP Starvation Tool

## ⚠️ CẢNH BÁO QUAN TRỌNG

**Công cụ này chỉ dành cho mục đích học tập và kiểm tra bảo mật trong môi trường được phép!**

- Chỉ sử dụng trong mạng LAN của bạn hoặc phòng lab
- Không sử dụng trên mạng không thuộc quyền sở hữu
- Việc sử dụng sai mục đích có thể vi phạm pháp luật

## Mô tả

DHCP Starvation là một kỹ thuật tấn công mạng nhằm làm cạn kiệt pool IP của DHCP server bằng cách gửi liên tục các gói DHCP Discover với các MAC address giả mạo. Điều này có thể khiến các thiết bị mới không thể lấy được IP từ DHCP server.

## Yêu cầu hệ thống

- **Hệ điều hành**: Windows
- **Python**: 3.6 trở lên
- **Thư viện**: Scapy
- **Quyền**: Administrator/Root privileges

## Cài đặt

### 1. Cài đặt Python
Tải và cài đặt Python từ [python.org](https://python.org)

### 2. Cài đặt Scapy
```bash
pip install scapy
```

### 3. Cài đặt Npcap (bắt buộc cho Windows)
- Tải Npcap từ [npcap.com](https://npcap.com/#download)
- Cài đặt với tùy chọn "Install Npcap in WinPcap API-compatible Mode"

## Cách sử dụng

### 1. Chạy chương trình
```bash
python dhcp_starvation.py
```

### 2. Chọn interface mạng
- Chương trình sẽ hiển thị danh sách các interface khả dụng
- Nhập số tương ứng với interface bạn muốn sử dụng
- Thường chọn interface Ethernet hoặc Wi-Fi chính

### 3. Theo dõi quá trình
- Chương trình sẽ bắt đầu gửi các gói DHCP Discover
- Mỗi gói có MAC address ngẫu nhiên
- Nhấn `Ctrl+C` để dừng

## Phân tích với Wireshark

### 1. Cài đặt Wireshark
Tải và cài đặt từ [wireshark.org](https://www.wireshark.org/download.html)

### 2. Bắt đầu capture
1. Mở Wireshark với quyền Administrator
2. Chọn interface mạng tương ứng (giống như trong Python script)
3. Nhấn nút "Start capturing packets" (biểu tượng shark fin)

### 3. Lọc gói tin DHCP
Trong thanh filter của Wireshark, nhập:
```
dhcp
```
hoặc
```
bootp
```

### 4. Phân tích gói tin

#### Gói DHCP Discover
- **Source**: 0.0.0.0 (client chưa có IP)
- **Destination**: 255.255.255.255 (broadcast)
- **UDP Port**: 68 → 67 (DHCP client → server)
- **MAC Address**: Thay đổi liên tục (fake MAC)
- **DHCP Message Type**: Discover (1)

#### Gói DHCP Offer (từ server)
- **Source**: IP của DHCP server
- **Destination**: 255.255.255.255
- **UDP Port**: 67 → 68
- **Offered IP**: IP được cấp phát
- **DHCP Message Type**: Offer (2)

### 5. Các chỉ số quan trọng cần theo dõi

#### Statistics → Protocol Hierarchy
- Xem tỷ lệ gói tin DHCP so với tổng traffic
- Thường thấy tăng đột biến khi chạy tool

#### Statistics → Conversations
- Xem số lượng conversation giữa các MAC address
- Phát hiện nhiều MAC address "mới" xuất hiện

#### DHCP Options Analysis
- **Option 53**: Message Type (1=Discover, 2=Offer, 3=Request, 5=ACK)
- **Option 61**: Client Identifier
- **Option 12**: Host Name

### 6. Dấu hiệu nhận biết tấn công

1. **Tần suất cao**: Nhiều gói DHCP Discover trong thời gian ngắn
2. **MAC address đa dạng**: Nhiều MAC khác nhau từ cùng một nguồn
3. **Pattern MAC**: MAC address có thể có pattern nhất định (như cùng OUI)
4. **Không có Request**: Chỉ thấy Discover mà không thấy Request tương ứng

## Các tính năng của script

### Tạo MAC address ngẫu nhiên
```python
def random_mac():
    mac = [0x00, 0x16, 0x3e,  # OUI cố định
           random.randint(0x00, 0x7f),
           random.randint(0x00, 0xff),
           random.randint(0x00, 0xff)]
```

### Tạo gói DHCP Discover
- Ethernet frame với src/dst MAC
- IP header (0.0.0.0 → 255.255.255.255)
- UDP header (port 68 → 67)
- BOOTP header với MAC address giả
- DHCP options (message-type: discover)

## Phòng chống

### 1. DHCP Snooping
- Bật DHCP snooping trên switch
- Cấu hình trusted/untrusted ports
- Giới hạn số lượng DHCP request per port

### 2. Port Security
- Giới hạn số lượng MAC address per port
- Sticky MAC learning
- Violation actions (shutdown, restrict, protect)

### 3. Rate Limiting
- Giới hạn tốc độ DHCP requests
- Cấu hình DHCP rate-limit trên router/switch

### 4. Monitoring
- Theo dõi DHCP pool utilization
- Cảnh báo khi pool gần cạn kiệt
- Log và phân tích DHCP transactions

## Kết luận

Công cụ này giúp hiểu rõ cách thức hoạt động của DHCP starvation attack và tầm quan trọng của việc bảo mật DHCP server. Sử dụng kết hợp với Wireshark để phân tích chi tiết các gói tin và hiểu sâu hơn về giao thức DHCP.

**Lưu ý**: Luôn thực hiện trong môi trường an toàn và có sự đồng ý của người quản trị mạng.