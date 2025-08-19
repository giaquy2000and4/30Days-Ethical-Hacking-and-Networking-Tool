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
    # URL local để test (giả sử bạn có server chạy tại http://127.0.0.1:5000)
    target_url = "http://127.0.0.1:5000"
    wordlist_file = "sample_wordlist.txt"

    dir_scan(target_url, wordlist_file)
