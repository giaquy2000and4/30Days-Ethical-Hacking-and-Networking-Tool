
# Dir Brute-Force Scanner (Local Demo)
Dự án này mô phỏng công cụ **directory brute-force** đơn giản, chạy trực tiếp trên máy local bằng **PyCharm**.  
Mục tiêu là giúp người học hiểu cách thức hoạt động của dir scanner trước khi áp dụng vào môi trường thật.

---

## 1. Yêu cầu hệ thống
- Python 3.x  
- PyCharm hoặc bất kỳ IDE Python nào  
- Thư viện: `requests`, `flask`

Cài đặt thư viện:
```bash
pip install requests flask
````

---

## 2. Cấu trúc thư mục

```
project/
│
├── dirscan.py            # Tool brute-force directories
├── server.py             # Flask server giả lập
├── sample_wordlist.txt   # Danh sách từ khóa brute-force
```

---

## 3. Nội dung các file

### `server.py`

Tạo server Flask giả lập:

```python
from flask import Flask
app = Flask(__name__)

@app.route("/")
def index():
    return "Home Page"

@app.route("/admin")
def admin():
    return "Admin Page"

@app.route("/dashboard")
def dashboard():
    return "Dashboard"

if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5000)
```

### `dirscan.py`

Tool brute-force directories:

```python
import requests

def dir_scan(url, wordlist):
    with open(wordlist, "r") as f:
        for line in f:
            path = line.strip()
            if not path:
                continue
            full_url = url.rstrip("/") + "/" + path
            try:
                r = requests.get(full_url)
                print(f"{full_url} -> {r.status_code}")
            except requests.RequestException as e:
                print(f"Error: {e}")

if __name__ == "__main__":
    target_url = "http://127.0.0.1:5000"
    wordlist_file = "sample_wordlist.txt"

    dir_scan(target_url, wordlist_file)
```

### `sample_wordlist.txt`

Danh sách các đường dẫn cần brute-force:

```
admin
login
dashboard
uploads
secret
```

---

## 4. Cách chạy mô phỏng

### Bước 1: Khởi động server giả lập

Trong terminal PyCharm, chạy:

```bash
python server.py
```

Server chạy tại `http://127.0.0.1:5000`.

### Bước 2: Chạy công cụ brute-force

Mở một terminal khác, chạy:

```bash
python dirscan.py
```

### Bước 3: Kết quả hiển thị

Ví dụ kết quả:

```
http://127.0.0.1:5000/admin -> 200
http://127.0.0.1:5000/login -> 404
http://127.0.0.1:5000/dashboard -> 200
http://127.0.0.1:5000/uploads -> 404
http://127.0.0.1:5000/secret -> 404
```

---

## 5. Lưu ý

* Đây chỉ là bản mô phỏng **local demo** để học tập.
* Khi áp dụng ra môi trường thực tế, cần xin phép và tuân thủ pháp luật.


