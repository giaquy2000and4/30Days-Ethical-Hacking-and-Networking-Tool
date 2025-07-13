# Windows MAC Changer Tool

Công cụ thay đổi địa chỉ MAC (Media Access Control) cho các giao diện mạng trên Windows.

## Mô tả

MAC Changer Tool là một công cụ Python cho phép bạn thay đổi địa chỉ MAC của các giao diện mạng trên hệ điều hành Windows. Công cụ này hỗ trợ tự động tạo MAC address ngẫu nhiên hoặc cho phép bạn nhập MAC address tùy chỉnh.

## Tính năng

- ✅ Liệt kê tất cả các giao diện mạng vật lý có sẵn
- ✅ Tự động tạo MAC address ngẫu nhiên hợp lệ
- ✅ Cho phép nhập MAC address tùy chỉnh
- ✅ Khởi động lại giao diện mạng tự động
- ✅ Kiểm tra và xác minh MAC address sau khi thay đổi
- ✅ Lọc bỏ các giao diện ảo (Virtual, VMware, Hyper-V, VPN)

## Yêu cầu hệ thống

- **Hệ điều hành**: Windows (Vista/7/8/10/11)
- **Python**: 3.6 trở lên
- **Quyền**: Administrator (bắt buộc)

## Cài đặt

### 1. Cài đặt Python dependencies

```bash
pip install wmi
```

### 2. Tải xuống file

```bash
git clone <repository-url>
cd mac-changer
```

hoặc tải trực tiếp file `mac_changer.py`

## Cách sử dụng

### 1. Chạy với quyền Administrator

**Quan trọng**: Phải chạy Command Prompt hoặc PowerShell với quyền Administrator

```bash
python dhcp_starvation.py
```

### 2. Chọn giao diện mạng

Chương trình sẽ hiển thị danh sách các giao diện mạng có sẵn:

```
Danh sách interface khả dụng:
0. Realtek PCIe GBE Family Controller
1. Intel(R) Wireless-AC 9560
```

Nhập số thứ tự của giao diện bạn muốn thay đổi MAC.

### 3. Nhập MAC address

- **Để tạo MAC ngẫu nhiên**: Nhấn Enter
- **Để nhập MAC tùy chỉnh**: Nhập 12 ký tự hex (ví dụ: `02A1B2C3D4E5`)

### 4. Xác minh kết quả

Chương trình sẽ:
- Hiển thị MAC address hiện tại
- Thay đổi MAC trong registry
- Khởi động lại giao diện mạng
- Kiểm tra và xác minh MAC address mới

## Ví dụ sử dụng

```
=== Windows MAC Changer Tool ===

Danh sách interface khả dụng:
0. Realtek PCIe GBE Family Controller

Chọn số thứ tự interface bạn muốn thay đổi MAC: 0
[+] Đã chọn: Realtek PCIe GBE Family Controller
Nhập MAC mới (hoặc Enter để tạo ngẫu nhiên): 

[+] MAC ngẫu nhiên được tạo: 02A1B2C3D4E5
[+] MAC hiện tại: AA:BB:CC:DD:EE:FF
[+] Tìm thấy adapter: Realtek PCIe GBE Family Controller
[+] Đổi MAC trong registry thành công. Đang khởi động lại interface...
[*] Đang disable interface...
[*] Đang enable interface...
[✓] MAC đã được đổi thành: 02A1B2C3D4E5
```

## Lưu ý quan trọng

### ⚠️ Cảnh báo
- **Luôn chạy với quyền Administrator**
- Việc thay đổi MAC address có thể ảnh hưởng đến kết nối mạng
- Một số card mạng có thể không hỗ trợ thay đổi MAC
- MAC address sẽ được reset về giá trị mặc định khi khởi động lại hệ thống

### 📋 Định dạng MAC hợp lệ
- MAC address phải có 12 ký tự hex
- Byte đầu tiên nên là `02` để đảm bảo là Locally Administered
- Ví dụ hợp lệ: `02A1B2C3D4E5`, `0234567890AB`

### 🔧 Khắc phục sự cố

**Lỗi "Không tìm thấy interface"**:
- Đảm bảo giao diện mạng đang hoạt động
- Kiểm tra tên giao diện mạng trong Device Manager

**Lỗi "Registry"**:
- Đảm bảo chạy với quyền Administrator
- Một số card mạng có thể không hỗ trợ thay đổi MAC

**MAC không thay đổi**:
- Thử khởi động lại máy tính
- Kiểm tra driver card mạng
- Thử với MAC address khác

## Tính pháp lý

Công cụ này được tạo ra cho mục đích học tập và kiểm thử hệ thống. Người dùng có trách nhiệm tuân thủ các quy định pháp luật và chính sách của tổ chức khi sử dụng.

## Giấy phép

Dự án này được phát hành dưới giấy phép MIT License.

## Đóng góp

Hoan nghênh các đóng góp! Vui lòng tạo issue hoặc pull request để báo cáo lỗi hoặc đề xuất tính năng mới.

## Liên hệ

Nếu bạn gặp vấn đề hoặc có câu hỏi, vui lòng tạo issue trên repository này.