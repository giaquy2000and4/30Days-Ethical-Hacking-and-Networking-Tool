# WiFi Scanner

Một công cụ đơn giản để quét và hiển thị danh sách các mạng Wi-Fi có sẵn trên Windows.

## Mô tả

Chương trình này sử dụng lệnh `netsh` của Windows để quét và hiển thị thông tin chi tiết về các mạng Wi-Fi xung quanh, bao gồm:
- **SSID**: Tên mạng Wi-Fi
- **Tín hiệu**: Cường độ tín hiệu (%)
- **Bảo mật**: Loại bảo mật (WPA2, WPA3, Open, v.v.)
- **Kênh**: Kênh phát sóng
- **BSSID**: Địa chỉ MAC của Access Point

## Yêu cầu hệ thống

- **Hệ điều hành**: Windows 7 trở lên
- **Python**: Phiên bản 3.6 trở lên
- **Quyền truy cập**: Có thể cần quyền Administrator để thực hiện một số lệnh

## Cài đặt

1. Đảm bảo Python đã được cài đặt trên máy tính
2. Tải xuống file `wifi_scanner.py`
3. Không cần cài đặt thêm thư viện nào (chỉ sử dụng thư viện chuẩn của Python)

## Cách sử dụng

### Chạy trực tiếp
```bash
python wifi_scanner.py
```

### Chạy từ Command Prompt với quyền Administrator (khuyến nghị)
1. Mở Command Prompt với quyền Administrator
2. Điều hướng đến thư mục chứa file
3. Chạy lệnh:
```bash
python wifi_scanner.py
```

## Kết quả hiển thị

Chương trình sẽ hiển thị bảng kết quả dưới dạng:

```
========================================================================
STT  SSID                     Tín hiệu   Bảo mật              Kênh 
========================================================================
1    MyWiFi                   85%        WPA2-Personal        6    
2    Neighbor_WiFi            45%        WPA2-Personal        11   
3    Guest_Network            60%        Open                 1    
========================================================================
```

## Xử lý lỗi

- **Lỗi netsh**: Nếu gặp lỗi "Không thể thực hiện lệnh netsh", hãy thử:
  - Chạy Command Prompt với quyền Administrator
  - Kiểm tra xem Wi-Fi adapter có được bật không
  - Khởi động lại dịch vụ WLAN AutoConfig

- **Không tìm thấy mạng**: Nếu hiển thị "Không tìm thấy mạng Wi-Fi nào":
  - Kiểm tra Wi-Fi adapter có hoạt động không
  - Đảm bảo có các mạng Wi-Fi xung quanh
  - Thử chạy lại sau vài giây

## Tính năng

- ✅ Quét tự động các mạng Wi-Fi có sẵn
- ✅ Hiển thị thông tin chi tiết về từng mạng
- ✅ Định dạng bảng dễ đọc
- ✅ Xử lý lỗi cơ bản
- ✅ Hỗ trợ tiếng Việt

## Giới hạn

- Chỉ hoạt động trên Windows
- Cần có Wi-Fi adapter để quét
- Một số thông tin có thể cần quyền Administrator
- Không hỗ trợ kết nối vào mạng Wi-Fi

## Đóng góp

Nếu bạn muốn đóng góp cho dự án:
1. Fork repository
2. Tạo branch mới cho tính năng
3. Commit các thay đổi
4. Tạo Pull Request

## Giấy phép

Dự án này được phát hành dưới giấy phép MIT.

## Liên hệ

Nếu có vấn đề hoặc đề xuất, vui lòng tạo issue trong repository.

---

*Lưu ý: Chương trình này chỉ dành cho mục đích học tập và sử dụng cá nhân. Vui lòng tuân thủ các quy định pháp luật về bảo mật mạng.*