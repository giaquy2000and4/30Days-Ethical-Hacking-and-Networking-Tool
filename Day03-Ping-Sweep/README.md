# Ping Sweep Tool

Công cụ quét ping đa luồng để kiểm tra các host đang hoạt động trong mạng.

## Mô tả

Công cụ này gửi các gói tin ICMP (ping) đến tất cả các địa chỉ IP trong một dải mạng được chỉ định (định dạng CIDR). Nó sử dụng thread pool để thực hiện công việc đồng thời, giúp tăng tốc đáng kể quá trình quét. Các IP phản hồi ping sẽ được coi là "alive" và được in ra console.

## Yêu cầu

- Python 3.x
- Quyền thực thi ping command trên hệ thống
- Hỗ trợ Windows, Linux và macOS

## Cài đặt

1. Tải xuống file `ping_sweep.py`
2. Đảm bảo Python 3 đã được cài đặt
3. Cấp quyền thực thi cho file (trên Linux/macOS):
   ```bash
   chmod +x ping_sweep.py
   ```

## Cách sử dụng

### Cú pháp cơ bản:
```bash
python ping_sweep.py <Network CIDR> [Số lượng threads]
```

### Ví dụ:

1. **Quét mạng 192.168.1.0/24 với 50 threads mặc định:**
   ```bash
   python ping_sweep.py 192.168.1.0/24
   ```

2. **Quét mạng 10.0.0.0/22 với 100 threads:**
   ```bash
   python ping_sweep.py 10.0.0.0/22 100
   ```

3. **Quét mạng con nhỏ:**
   ```bash
   python ping_sweep.py 192.168.1.0/28 20
   ```

## Tham số

- **Network CIDR** (bắt buộc): Dải mạng cần quét ở định dạng CIDR (ví dụ: 192.168.1.0/24)
- **Số lượng threads** (tùy chọn): Số thread worker sử dụng (mặc định: 50)

## Đặc điểm

- **Đa luồng**: Sử dụng ThreadPoolExecutor để quét song song nhiều IP
- **Đa nền tảng**: Hoạt động trên Windows, Linux và macOS
- **Hiệu suất cao**: Có thể quét hàng trăm host trong vài giây
- **An toàn thread**: Sử dụng lock để đồng bộ hóa output
- **Xử lý lỗi**: Bắt và báo cáo lỗi một cách graceful

## Kết quả mẫu

```
[INFO] Starting scan on network: 192.168.1.0/24 (254 hosts)
[INFO] Using 50 worker threads...

[+] 192.168.1.1     - Host is alive
[+] 192.168.1.10    - Host is alive
[+] 192.168.1.25    - Host is alive
[+] 192.168.1.100   - Host is alive

========================================
      SCAN COMPLETE
========================================

[✓] Found 4 live hosts:
    - 192.168.1.1
    - 192.168.1.10
    - 192.168.1.25
    - 192.168.1.100
```

## Tối ưu hóa hiệu suất

- **Cho mạng /24** (254 hosts): Sử dụng 50-100 threads
- **Cho mạng lớn hơn** (/22, /20): Có thể tăng lên 100-200 threads
- **Cho mạng nhỏ** (/28, /29): Sử dụng 10-20 threads

**Lưu ý**: Quá nhiều threads có thể gây quá tải hệ thống hoặc bị firewall chặn.

## Cách thức hoạt động

1. **Phân tích tham số**: Xử lý network CIDR và số lượng threads
2. **Tạo danh sách IP**: Sử dụng `ipaddress.ip_network()` để tạo danh sách tất cả host
3. **Quét đa luồng**: Mỗi thread thực hiện ping một IP
4. **Thu thập kết quả**: Tổng hợp các IP phản hồi
5. **Hiển thị kết quả**: Sắp xếp và in danh sách host đang hoạt động

## Xử lý lỗi

Công cụ xử lý các tình huống lỗi phổ biến:
- CIDR không hợp lệ
- Số lượng threads không hợp lệ
- Lỗi khi thực thi ping command
- Lỗi quyền truy cập

## Hạn chế

- Một số firewall có thể chặn ICMP packets
- Cần quyền admin/root trên một số hệ thống
- Hiệu suất phụ thuộc vào network latency
- Một số host có thể cấu hình không phản hồi ping

## Bảo mật

Công cụ này chỉ thực hiện ping (ICMP) và không thực hiện:
- Port scanning
- Vulnerability testing
- Network intrusion
- Data collection

Hãy sử dụng có trách nhiệm và tuân thủ các quy định về bảo mật mạng.

## Giấy phép

Công cụ này được cung cấp "như là" cho mục đích giáo dục và quản trị mạng hợp pháp.
