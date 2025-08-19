
# XSS Payload Tester
This project provides a simple environment to demonstrate and test Cross-Site Scripting (XSS) vulnerabilities. It consists of two main components:
1. A local web server built with Flask, exposing intentionally vulnerable and filtered endpoints.
2. A Python-based XSS Payload Tester that automatically submits payloads to form inputs and analyzes responses.

---

## Features

- Detects if payloads are reflected raw, escaped, or stripped.
- Supports GET and POST form submissions.
- Uses predefined payloads or a custom payload file.
- Easy to extend with additional payloads.
- Provides three types of local servers for different behaviors:
  - Vulnerable (reflected without sanitization)
  - Escaped (HTML-encoded output)
  - Stripped (basic removal of dangerous tags)

---

## Requirements

- Python 3.8 or higher
- Dependencies:
```bash
  pip install flask requests beautifulsoup4
````

---

## Local Server Setup

Three server variants are included for testing.

### 1. Vulnerable Server (`app.py`)

Reflects input directly into the response without sanitization. Useful for testing raw reflected XSS.

Run:

```bash
python app.py
```

Available at: `http://127.0.0.1:8000/`

### 2. Escaped Server (`app_filter.py`)

Escapes special characters (`<`, `>`, `&`, `"`, `'`) using `escape()`. Input is reflected but HTML-encoded.

Run:

```bash
python app_filter.py
```

Available at: `http://127.0.0.1:8001/`

### 3. Stripped Server (`app_strip.py`)

Removes known dangerous tags such as `<script>`, `<img>`, `<svg>`, `<iframe>` using regular expressions.

Run:

```bash
python app_strip.py
```

Available at: `http://127.0.0.1:8002/`

---

## XSS Payload Tester

The testing script automatically submits payloads to form fields and evaluates the response.

### Usage

```bash
python xss_tester.py -u <target_url>
```

Example:

```bash
python xss_tester.py -u http://127.0.0.1:8000/
```

### Options

* `-u, --url` (required): Target URL to test.
* `-p, --payloads`: Path to a file containing custom payloads (one per line). If omitted, default payloads are used.

---

## Example Output

Running against the vulnerable server:

```
[+] Found 1 form(s) at http://127.0.0.1:8000/

[*] Testing form #1 -> http://127.0.0.1:8000/ [get]
   Payload: <script>alert(1)</script> -> reflected-raw
   Payload: "><script>alert(1)</script> -> reflected-raw
   Payload: <img src=x onerror=alert(1)> -> reflected-raw
   Payload: <svg/onload=alert(1)> -> reflected-raw
   Payload: ';alert(1);// -> reflected-raw
```

---

## Project Structure

```
Day20-XSS-Payload-Tester/
│
├── app.py           # Vulnerable server
├── app_filter.py    # Escaped server
├── app_strip.py     # Stripped server
├── xss_tester.py    # XSS Payload Tester
└── README.md        # Documentation
```

---

## Notes

* This project is intended for educational and testing purposes only.
* Run servers only on a local environment.
* Do not use this tool against systems you do not own or lack explicit permission to test.

