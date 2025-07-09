 # Traceroute Tool

Công cụ traceroute sử dụng Scapy và Graphviz để theo dõi đường đi gói tin mạng và tạo biểu đồ trực quan.

## Mô tả

Chương trình này thực hiện chức năng traceroute để theo dõi đường đi của gói tin từ máy tính của bạn đến một đích cụ thể (domain name hoặc địa chỉ IP). Kết quả sẽ được hiển thị dưới dạng text và có thể tạo ra biểu đồ trực quan cho dễ theo dõi.

## Tính năng

- ✅ Theo dõi đường đi gói tin đến đích
- ✅ Hiển thị thời gian phản hồi (RTT) cho mỗi hop
- ✅ Tạo biểu đồ trực quan bằng Graphviz
- ✅ Hỗ trợ cả domain name và địa chỉ IP
- ✅ Tùy chỉnh số hop tối đa và timeout
- ✅ Xử lý timeout và các lỗi mạng

## Yêu cầu hệ thống

### Python Dependencies
```bash
pip install scapy
pip install graphviz
```

### Phần mềm bổ sung
- **Graphviz**: Cần cài đặt Graphviz để tạo biểu đồ
  - **Windows**: Tải từ https://graphviz.org/download/
  - **Linux**: `sudo apt-get install graphviz` (Ubuntu/Debian) hoặc `sudo yum install graphviz` (CentOS/RHEL)
  - **macOS**: `brew install graphviz`

### Quyền Admin
Chương trình cần quyền Administrator/root để gửi gói tin ICMP:
- **Windows**: Chạy từ Command Prompt/PowerShell với quyền Administrator
- **Linux/macOS**: Chạy với `sudo`

## Cài đặt

1. Clone hoặc tải xuống file `trace_route.py`
2. Cài đặt các thư viện Python cần thiết:
   ```bash
   pip install scapy graphviz
   ```
3. Cài đặt Graphviz software (xem phần Yêu cầu hệ thống)

## Cách sử dụng

### Cú pháp cơ bản
```bash
python trace_route.py <đích>
```

### Cú pháp đầy đủ
```bash
python trace_route.py <đích> [--max-hops <số>] [--timeout <giây>]
```

### Các tham số

- `đích`: Địa chỉ IP hoặc domain name của đích cần traceroute
- `--max-hops`: Số hop tối đa (mặc định: 30)
- `--timeout`: Thời gian chờ phản hồi cho mỗi hop (mặc định: 2 giây)

### Ví dụ sử dụng

```bash
# Traceroute đến Google
python trace_route.py google.com

# Traceroute với số hop tối đa là 20
python trace_route.py facebook.com --max-hops 20

# Traceroute với timeout 5 giây
python trace_route.py 8.8.8.8 --timeout 5

# Chạy với quyền admin (Linux/macOS)
sudo python trace_route.py google.com

# Chạy với quyền admin (Windows)
# Mở Command Prompt/PowerShell với quyền Administrator, sau đó:
python trace_route.py google.com
```

## Kết quả đầu ra

### Console Output
```
Traceroute to google.com (142.250.191.14), max 30 hops:

 1      192.168.1.1  2.45 ms
 2      10.0.0.1     15.32 ms
 3      203.162.4.1  25.67 ms
 4      *            Request timed out.
 5      142.250.191.14  45.23 ms

Trace complete.
```

### Biểu đồ trực quan
Chương trình sẽ tạo file PNG hiển thị đường đi dưới dạng biểu đồ với:
- Nút xanh lá: Máy tính của bạn
- Nút xanh dương: Các hop trung gian
- Nút đỏ: Hop timeout
- Nút vàng: Đích đến

## Cấu trúc code

### Hàm chính

- `run_traceroute(target, max_hops, timeout)`: Thực hiện traceroute
- `draw_route_graph(hops_data, output_filename)`: Tạo biểu đồ từ kết quả traceroute

### Xử lý lỗi

- Xử lý domain name không hợp lệ
- Xử lý timeout cho từng hop
- Xử lý lỗi khi không tìm thấy Graphviz
- Xử lý các lỗi mạng khác

## Lưu ý quan trọng

1. **Quyền Admin**: Bắt buộc phải có quyền admin để gửi gói tin ICMP
2. **Firewall**: Một số firewall có thể chặn gói tin ICMP
3. **Mạng công ty**: Một số mạng công ty có thể chặn hoặc hạn chế traceroute
4. **Độ chính xác**: Kết quả có thể khác nhau giữa các lần chạy do tình trạng mạng

## Khắc phục sự cố

### Lỗi phổ biến

1. **"Permission denied"**: Chạy với quyền admin
2. **"Graphviz executable not found"**: Cài đặt Graphviz và thêm vào PATH
3. **"Could not resolve domain name"**: Kiểm tra kết nối internet và tên domain
4. **Timeout nhiều hop**: Tăng giá trị timeout hoặc kiểm tra kết nối mạng

### Gỡ lỗi

Nếu gặp vấn đề, bạn có thể:
1. Kiểm tra kết nối internet
2. Thử với địa chỉ IP thay vì domain name
3. Tăng giá trị timeout
4. Kiểm tra tường lửa và antivirus

## Tác giả

Chương trình sử dụng:
- **Scapy**: Thư viện Python cho việc xử lý gói tin mạng
- **Graphviz**: Công cụ tạo biểu đồ

## Giấy phép

Chương trình này được phát triển cho mục đích học tập và nghiên cứu. Vui lòng tuân thủ các quy định về sử dụng công cụ mạng tại địa phương của bạn.
