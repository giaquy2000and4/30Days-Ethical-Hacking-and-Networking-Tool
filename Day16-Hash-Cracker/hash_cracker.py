import hashlib
import itertools
import string
import os

def hash_string(text, algo):
    text = text.encode()
    if algo == "md5":
        return hashlib.md5(text).hexdigest()
    elif algo == "sha1":
        return hashlib.sha1(text).hexdigest()
    elif algo == "sha256":
        return hashlib.sha256(text).hexdigest()
    else:
        print("[!] Thuật toán không hỗ trợ.")
        return None

def create_wordlist(filename, min_len, max_len, charset):
    if charset == "lower":
        chars = string.ascii_lowercase
    elif charset == "upper":
        chars = string.ascii_uppercase
    elif charset == "digits":
        chars = string.digits
    elif charset == "mix":
        chars = string.ascii_letters + string.digits
    else:
        chars = charset  # custom nhập tay

    print(f"[*] Đang tạo wordlist ({min_len}-{max_len} ký tự)...")
    with open(filename, "w", encoding="utf-8") as f:
        for length in range(min_len, max_len + 1):
            for combo in itertools.product(chars, repeat=length):
                f.write("".join(combo) + "\n")
    print(f"[+] Wordlist đã lưu tại: {filename}")

def generate_hash():
    text = input("Nhập chuỗi cần mã hóa: ")
    algo = input("Chọn thuật toán (md5 / sha1 / sha256): ").lower()
    hashed = hash_string(text, algo)
    if hashed:
        print(f"[+] {algo.upper()} của '{text}' là:\n{hashed}")

def crack_hash():
    hash_input = input("Nhập hash cần dò: ").lower()
    algo = input("Thuật toán hash (md5 / sha1 / sha256): ").lower()
    wordlist = input("Nhập đường dẫn đến file wordlist: ")

    if not os.path.exists(wordlist):
        print("[!] Không tìm thấy file wordlist.")
        return

    print("[*] Đang dò hash...")
    with open(wordlist, "r", encoding="utf-8", errors="ignore") as f:
        for line in f:
            word = line.strip()
            if hash_string(word, algo) == hash_input:
                print(f"[+] Đã tìm thấy! Giá trị gốc là: {word}")
                return
    print("[-] Không tìm thấy chuỗi phù hợp trong wordlist.")

def menu():
    while True:
        print("\n==== HASH TOOL MENU ====")
        print("1. Tạo wordlist")
        print("2. Tạo hash từ chuỗi")
        print("3. Crack hash bằng wordlist")
        print("0. Thoát")
        choice = input("Chọn chức năng (0-3): ")

        if choice == "1":
            filename = input("Tên file wordlist: ")
            min_len = int(input("Độ dài tối thiểu: "))
            max_len = int(input("Độ dài tối đa: "))
            print("Chọn kiểu ký tự:")
            print(" - lower  → a-z")
            print(" - upper  → A-Z")
            print(" - digits → 0-9")
            print(" - mix    → a-zA-Z0-9")
            charset = input("Nhập kiểu ký tự: ").lower()
            create_wordlist(filename, min_len, max_len, charset)
        elif choice == "2":
            generate_hash()
        elif choice == "3":
            crack_hash()
        elif choice == "0":
            print("Tạm biệt!")
            break
        else:
            print("Lựa chọn không hợp lệ!")

if __name__ == "__main__":
    menu()
