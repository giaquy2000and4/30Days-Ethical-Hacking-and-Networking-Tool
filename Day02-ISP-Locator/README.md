# ISP Locator

## Mô tả

ISP Locator là một công cụ Python đơn giản giúp hiển thị thông tin về địa chỉ IP công cộng và nhà cung cấp dịch vụ Internet (ISP) của bạn. Công cụ này sử dụng API của ipinfo.io để lấy thông tin chi tiết về kết nối mạng hiện tại.

## Tính năng

- ✅ Hiển thị địa chỉ IP công cộng
- ✅ Thông tin nhà cung cấp dịch vụ Internet (ISP/Organization)
- ✅ Vị trí địa lý (thành phố, tỉnh/bang)
- ✅ Tùy chọn hiển thị mã quốc gia
- ✅ Tùy chọn hiển thị thông tin ASN (Autonomous System Number)
- ✅ Xử lý lỗi mạnh mẽ với timeout và exception handling

## Yêu cầu hệ thống

- Python 3.6 trở lên
- Thư viện `requests`
- Kết nối Internet

## Cài đặt

1. **Clone hoặc tải xuống file:**
   ```bash
   # Tải xuống file isp_locator.py
   ```

2. **Cài đặt thư viện cần thiết:**
   ```bash
   pip install requests
   ```

   Hoặc nếu bạn có file requirements.txt:
   ```bash
   pip install -r requirements.txt
   ```

## Cách sử dụng

### Sử dụng cơ bản

```bash
python isp_locator.py
```

Kết quả mẫu:
```
Fetching your IP information...

==============================
  PUBLIC IP INFORMATION
==============================
[*] Public IP:      203.xxx.xxx.xxx
[*] ISP / Org:      AS18403 The Viettel Group
[*] Location:       Hanoi, Hanoi
==============================
```

### Các tùy chọn nâng cao

**Hiển thị mã quốc gia:**
```bash
python isp_locator.py --country
```

**Hiển thị thông tin ASN:**
```bash
python isp_locator.py --asn
```

**Sử dụng kết hợp các tùy chọn:**
```bash
python isp_locator.py --country --asn
```

### Trợ giúp

Để xem tất cả các tùy chọn có sẵn:
```bash
python isp_locator.py --help
```

## Tham số dòng lệnh

| Tham số | Mô tả |
|---------|-------|
| `--country` | Hiển thị mã quốc gia (ví dụ: US, VN) |
| `--asn` | Hiển thị thông tin ASN (Autonomous System Number) |
| `--help` | Hiển thị thông tin trợ giúp |

## Xử lý lỗi

Công cụ này xử lý các lỗi phổ biến:

- **Lỗi kết nối mạng**: Kiểm tra kết nối Internet của bạn
- **Timeout**: Mặc định là 10 giây, có thể do mạng chậm
- **Rate limit**: API ipinfo.io có giới hạn số lượng request
- **Dữ liệu thiếu**: Sử dụng giá trị mặc định 'N/A' nếu thông tin không có

## API được sử dụng

Công cụ này sử dụng API miễn phí của [ipinfo.io](https://ipinfo.io/):
- **Endpoint**: `https://ipinfo.io/json`
- **Phương thức**: GET
- **Định dạng**: JSON
- **Giới hạn**: 50,000 requests/tháng cho tài khoản miễn phí

## Ví dụ kết quả

```bash
$ python isp_locator.py --country --asn

Fetching your IP information...

==============================
  PUBLIC IP INFORMATION
==============================
[*] Public IP:      203.113.xxx.xxx
[*] ISP / Org:      AS18403 The Viettel Group
[*] Location:       Ho Chi Minh City, Ho Chi Minh
[*] Country:        VN
[*] ASN Info:       AS18403 The Viettel Group
==============================
```

## Lưu ý bảo mật

- Công cụ này chỉ hiển thị thông tin IP công cộng, không thu thập dữ liệu cá nhân
- Không lưu trữ thông tin trên máy tính local
- Thông tin được lấy từ API bên thứ ba (ipinfo.io)

## Khắc phục sự cố

### Lỗi "Could not connect to the ipinfo.io service"
- Kiểm tra kết nối Internet
- Kiểm tra firewall hoặc proxy
- Thử lại sau vài phút

### Lỗi "ModuleNotFoundError: No module named 'requests'"
```bash
pip install requests
```

### Lỗi timeout
- Kiểm tra tốc độ mạng
- Thử lại sau ít phút

## Đóng góp

Nếu bạn muốn đóng góp cải thiện công cụ này:

1. Fork dự án
2. Tạo branch mới (`git checkout -b feature/amazing-feature`)
3. Commit thay đổi (`git commit -m 'Add some amazing feature'`)
4. Push lên branch (`git push origin feature/amazing-feature`)
5. Tạo Pull Request

## Giấy phép

Dự án này được phát hành dưới giấy phép MIT. Xem file `LICENSE` để biết thêm chi tiết.

## Liên hệ

Nếu có bất kỳ câu hỏi hoặc góp ý nào, vui lòng tạo issue trên GitHub repository.

---

**Lưu ý**: Công cụ này chỉ dành cho mục đích giáo dục và sử dụng cá nhân. Vui lòng tuân thủ điều khoản sử dụng của API ipinfo.io.
