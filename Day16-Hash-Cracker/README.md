
#  Hash Cracker Tool

Một công cụ dòng lệnh đơn giản bằng Python giúp bạn:

- ✅ Tạo wordlist tùy chỉnh (a-z, A-Z, 0-9,...)
- ✅ Tạo hash từ chuỗi người dùng nhập (MD5, SHA1, SHA256)
- ✅ Crack hash bằng wordlist

---

##  Yêu cầu

- Python 3.6+
- Không cần thư viện ngoài

---

##  Cách chạy

```bash
python hash_cracker.py
````

Bạn sẽ thấy menu:

```
==== HASH TOOL MENU ====
1. Tạo wordlist
2. Tạo hash từ chuỗi
3. Crack hash bằng wordlist
0. Thoát
```

---

##  Ví dụ sử dụng

### 1. Tạo wordlist

```
Chọn chức năng: 1
Tên file wordlist: wordlist.txt
Độ dài tối thiểu: 3
Độ dài tối đa: 4
Kiểu ký tự: lower
```

→ Tạo `wordlist.txt` gồm các chuỗi từ `aaa` đến `zzzz`

---

### 2. Tạo hash từ chuỗi

```
Chọn chức năng: 2
Nhập chuỗi cần mã hóa: hello
Chọn thuật toán: md5
```

→ Kết quả:

```
[+] MD5 của 'hello' là:
5d41402abc4b2a76b9719d911017c592
```

---

### 3. Crack hash bằng wordlist

```
Chọn chức năng: 3
Nhập hash cần dò: 5d41402abc4b2a76b9719d911017c592
Thuật toán hash: md5
Nhập đường dẫn đến file wordlist: wordlist.txt
```

→ Nếu từ "hello" có trong wordlist:

```
[+] Đã tìm thấy! Giá trị gốc là: hello
```

---

## ⚠️ Lưu ý hiệu suất

* Tránh tạo wordlist quá lớn (ví dụ: 5-7 ký tự + `mix`) vì có thể sinh ra hàng trăm triệu dòng.
* Với charset `mix` (a-zA-Z0-9):

  * 5 ký tự: \~ 916 triệu dòng
  * Nên giới hạn độ dài hoặc chỉ dùng `lower`.

---

##  Giấy phép

Dùng cho mục đích học tập và kiểm thử bảo mật có kiểm soát (ethical hacking only).
Không sử dụng vào mục đích tấn công trái phép.

