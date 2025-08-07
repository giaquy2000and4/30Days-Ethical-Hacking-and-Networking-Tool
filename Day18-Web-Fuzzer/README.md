
# Web Fuzzer

Công cụ Web Fuzzer hỗ trợ dò tìm các tài nguyên ẩn trên một website bằng cách gửi các yêu cầu HTTP GET đến các đường dẫn phổ biến được liệt kê trong một wordlist. Mục tiêu chính của công cụ là hỗ trợ quá trình kiểm thử xâm nhập (penetration testing) và đánh giá bảo mật web bằng cách phát hiện các endpoint có thể bị bỏ sót.

## 1. Tính năng

- Hỗ trợ gửi yêu cầu GET đến danh sách các đường dẫn được chỉ định.
- Ghi nhận các phản hồi có mã trạng thái HTTP đáng chú ý (200, 301, 302, 403).
- Tự động chuẩn hóa và phân tích URL đầu vào để đảm bảo kết quả chính xác.
- Tương thích với hầu hết các trang web sử dụng giao thức HTTP hoặc HTTPS.

## 2. Yêu cầu hệ thống

- Python 3.6 hoặc cao hơn
- Thư viện `requests` (cài đặt bằng `pip install requests`)

## 3. Cài đặt

```bash
git clone https://github.com/ten-repo/web-fuzzer.git
cd web-fuzzer
pip install -r requirements.txt
````

**Ghi chú:** Nếu không có tệp `requirements.txt`, người dùng có thể cài đặt thủ công:

```bash
pip install requests
```

## 4. Cấu trúc thư mục

```
web_fuzzer/
├── fuzzer.py           # Tập tin chính chứa mã nguồn của công cụ
└── wordlist.txt        # Tệp văn bản chứa các đường dẫn cần dò tìm
```

## 5. Hướng dẫn sử dụng

Cú pháp tổng quát:

```bash
python fuzzer.py <url> <wordlist>
```

Trong đó:

* `<url>`: Địa chỉ trang web mục tiêu, bao gồm giao thức (ví dụ: `http://example.com`)
* `<wordlist>`: Đường dẫn đến tệp chứa danh sách các đường dẫn cần kiểm tra

### Ví dụ:

```bash
python fuzzer.py https://qldaotao.utehy.edu.vn/DangNhap/Login wordlist.txt
```

Công cụ sẽ tiến hành dò tìm theo các đường dẫn như:

* [https://qldaotao.utehy.edu.vn/admin](https://qldaotao.utehy.edu.vn/admin)
* [https://qldaotao.utehy.edu.vn/login](https://qldaotao.utehy.edu.vn/login)
* [https://qldaotao.utehy.edu.vn/dashboard](https://qldaotao.utehy.edu.vn/dashboard)
* ...

và hiển thị các kết quả có mã trạng thái phản hồi phù hợp.

## 6. Định dạng tệp wordlist

Mỗi dòng trong tệp `wordlist.txt` chứa một đường dẫn cần kiểm tra, **không có dấu gạch chéo đầu dòng**:

```
admin
login
dashboard
config
secret
```

## 7. Mã nguồn chính (`fuzzer.py`)

Mã nguồn được thiết kế theo hướng đơn giản, dễ mở rộng. Có thể tham khảo nội dung tệp `fuzzer.py` trong thư mục dự án để tùy chỉnh theo nhu cầu.

## 8. Đề xuất mở rộng

* Hỗ trợ gửi song song nhiều yêu cầu (đa luồng hoặc bất đồng bộ)
* Hỗ trợ giao thức POST hoặc HEAD
* Tùy chọn lọc phản hồi theo mã trạng thái hoặc tiêu đề HTTP
* Tích hợp thanh tiến trình hoặc xuất kết quả ra tệp

## 9. Cảnh báo và lưu ý pháp lý

Công cụ này được phát triển cho mục đích giáo dục và kiểm thử hợp pháp. Người sử dụng phải đảm bảo có sự cho phép rõ ràng từ chủ sở hữu hệ thống mục tiêu trước khi sử dụng công cụ. Mọi hành vi lạm dụng có thể vi phạm pháp luật và bị xử lý theo quy định hiện hành.

