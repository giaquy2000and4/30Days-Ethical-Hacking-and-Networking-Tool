import requests
import argparse
from urllib.parse import urlparse

def fuzz(domain, wordlist_file):
    with open(wordlist_file, 'r') as f:
        paths = [line.strip() for line in f if line.strip()]

    parsed = urlparse(domain)
    base_url = f"{parsed.scheme}://{parsed.netloc}"
    print(f"[+] Bắt đầu fuzzing trên: {base_url}")

    for path in paths:
        url = base_url + '/' + path.lstrip('/')
        try:
            response = requests.get(url, timeout=5)
            if response.status_code in [200, 301, 302, 403]:
                print(f"[+] {url} -> {response.status_code}")
        except requests.RequestException:
            continue

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Web Fuzzer - Dò tìm tài nguyên ẩn")
    parser.add_argument("domain", help="Tên miền (VD: http://example.com)")
    parser.add_argument("wordlist", help="Đường dẫn tới file wordlist")

    args = parser.parse_args()
    fuzz(args.domain, args.wordlist)
