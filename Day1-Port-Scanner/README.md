# Py PortScan

Một công cụ quét cổng đơn giản, nhanh chóng và đa luồng được viết bằng Python. Công cụ này cho phép bạn quét các cổng mở trên các máy chủ đích với các tùy chọn phạm vi cổng và luồng có thể tùy chỉnh.

## Tính năng

- **Quét đa luồng** để hiệu suất nhanh hơn
- **Phạm vi cổng tùy chỉnh** (các cổng cụ thể, phạm vi, hoặc các cổng phổ biến)
- **Phát hiện dịch vụ** cho các cổng phổ biến
- **Đầu ra có màu sắc** để dễ đọc hơn
- **Banner ASCII** với giao diện được tạo kiểu
- **Hỗ trợ phân giải tên máy chủ**
- **Luồng có thể cấu hình** để tối ưu hiệu suất

## Yêu cầu

- Python 3.6+
- Các gói cần thiết:
  - `colorama` - Để đầu ra terminal có màu
  - `pyfiglet` - Để tạo banner ASCII

## Cài đặt

1. Clone hoặc tải xuống script
2. Cài đặt các dependencies cần thiết:

```bash
pip install colorama pyfiglet
```

## Cách sử dụng

### Sử dụng cơ bản

```bash
python port_scan.py <target>
```

### Tùy chọn dòng lệnh

```bash
python port_scan.py [-h] [-p PORTS] [-t THREADS] target
```

#### Tham số

- `target` - Địa chỉ IP hoặc tên máy chủ cần quét (bắt buộc)
- `-p, --ports` - Chỉ định các cổng cần quét (tùy chọn)
- `-t, --threads` - Số lượng luồng cho việc quét (mặc định: 50)
- `-h, --help` - Hiển thị thông báo trợ giúp

### Ví dụ

#### Quét các cổng phổ biến (hành vi mặc định)
```bash
python port_scan.py 192.168.1.1
```

#### Quét một phạm vi cổng cụ thể
```bash
python port_scan.py 192.168.1.1 -p 1-1024
```

#### Quét các cổng cụ thể
```bash
python port_scan.py 192.168.1.1 -p 80,443,8080
```

#### Quét với số lượng luồng tùy chỉnh
```bash
python port_scan.py 192.168.1.1 -p 1-1000 -t 100
```

#### Quét một tên máy chủ
```bash
python port_scan.py google.com -p 80,443
```

## Các cổng phổ biến được phát hiện

Scanner bao gồm phát hiện dịch vụ cho các cổng phổ biến:

| Cổng | Dịch vụ |
|------|---------|
| 20   | FTP (Data) |
| 21   | FTP (Control) |
| 22   | SSH |
| 23   | Telnet |
| 25   | SMTP |
| 53   | DNS |
| 80   | HTTP |
| 110  | POP3 |
| 143  | IMAP |
| 443  | HTTPS |
| 445  | SMB |
| 993  | IMAPS |
| 995  | POP3S |
| 1433 | MSSQL |
| 3306 | MySQL |
| 3389 | RDP |
| 5432 | PostgreSQL |
| 5900 | VNC |
| 8080 | HTTP Proxy |

*Và nhiều hơn nữa...*

## Định dạng đầu ra

Scanner cung cấp đầu ra rõ ràng, có màu sắc hiển thị:
- Địa chỉ IP đích
- Số lượng cổng đã quét
- Số lượng luồng được sử dụng
- Bảng kết quả quét với các cột CỔNG, TRẠNG THÁI và DỊCH VỤ
- Tổng thời gian quét

### Ví dụ đầu ra
```
     ____            ____            __  _____                 
    / __ \__  __    / __ \____  ____/ /_/ ___/__________ _____ 
   / /_/ / / / /   / /_/ / __ \/ __  __/\__ \/ ___/ __ `/ __ \
  / ____/ /_/ /   / ____/ /_/ / /_/ /  ___/ / /__/ /_/ / / / /
 /_/    \__, /   /_/    \____/\__,_/  /____/\___/\__,_/_/ /_/ 
       /____/                                                 

Một công cụ quét cổng đa luồng đơn giản bởi BOCCHI89

Đang quét 192.168.1.1...
Các cổng cần quét: 30
Luồng: 50

--------------------------------------------------
Kết quả quét cho 192.168.1.1:
CỔNG      TRẠNG THÁI    DỊCH VỤ
----      -----------    -------
22        MỞ            SSH
80        MỞ            HTTP
443       MỞ            HTTPS
--------------------------------------------------
Hoàn thành quét trong 2.45 giây.
```

## Ghi chú về hiệu suất

- **Số lượng luồng**: Mặc định 50 luồng hoạt động tốt cho hầu hết các trường hợp. Bạn có thể tăng số này để quét nhanh hơn, nhưng hãy chú ý đến tài nguyên hệ thống và giới hạn mạng.
- **Timeout**: Mỗi lần thử kết nối cổng có timeout 0.5 giây để cân bằng giữa tốc độ và độ chính xác.
- **Phạm vi cổng**: Quét các phạm vi cổng lớn (1-65535) sẽ mất nhiều thời gian hơn. Hãy xem xét quét các cổng phổ biến trước.

## Giới hạn

- Công cụ này chỉ dành cho mục đích giáo dục và kiểm tra được ủy quyền
- Một số tường lửa có thể phát hiện hoạt động quét cổng
- Kết quả có thể thay đổi tùy thuộc vào điều kiện mạng và cấu hình máy chủ đích
- Chỉ quét các cổng TCP (không hỗ trợ quét UDP)

## Tuyên bố pháp lý

Công cụ này chỉ nên được sử dụng trên các mạng và hệ thống mà bạn sở hữu hoặc có sự cho phép rõ ràng để kiểm tra. Việc quét cổng trái phép có thể vi phạm luật pháp và quy định địa phương. Tác giả không chịu trách nhiệm về việc sử dụng sai mục đích của công cụ này.

## Tác giả

Được tạo bởi BOCCHI89

## Giấy phép

Dự án này được cung cấp như hiện tại cho mục đích giáo dục. Sử dụng một cách có trách nhiệm và tuân theo luật pháp và quy định hiện hành.

## Đóng góp

Vui lòng gửi issues, yêu cầu tính năng hoặc pull requests để cải thiện công cụ này.

---

**Lưu ý**: Luôn đảm bảo bạn có sự ủy quyền thích hợp trước khi quét bất kỳ mạng hoặc hệ thống nào mà bạn không sở hữu.
