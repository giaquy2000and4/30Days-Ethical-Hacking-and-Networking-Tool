
# SQL Injection Tester

This project provides a simple **SQL Injection (SQLi) testing tool** and a deliberately vulnerable web application for safe experimentation in a local environment.  
It is intended for **educational and lab purposes only**. Do not use this tool against systems you do not own or have explicit permission to test.

---

## Components

### 1. `vulnerable_app.py`
A minimal Flask web application that simulates an SQL injection vulnerability.  

- Exposes an endpoint `/search?q=` that directly concatenates user input into an SQL query without sanitization.  
- Uses SQLite for storage, making it lightweight and easy to run locally.  
- Returns SQL errors to the client, simulating a common insecure development environment.

**Usage:**
```bash
python vulnerable_app.py
````

By default, the application runs on:

```
http://127.0.0.1:5000
```

Example request:

```
http://127.0.0.1:5000/search?q=alice
```

---

### 2. `sqli_tester.py`

A command-line tool that sends a list of common SQLi payloads to a target URL and analyzes the responses.

**Key features:**

* Error-based detection: checks for common SQL error messages in the response.
* Boolean-based detection: compares responses from always-true vs always-false conditions.
* Time-based detection: measures response delays when using payloads with `SLEEP()` (works with MySQL/PostgreSQL, not SQLite).
* Heuristic analysis: evaluates HTTP status code changes and response length differences.

**Usage:**

```bash
python sqli_tester.py -u "http://127.0.0.1:5000/search?q=INJECT_HERE"
```

Options:

* `-u` / `--url`: Target URL with `INJECT_HERE` placeholder where payloads will be inserted.
* `-t` / `--timeout`: Request timeout (default: 6s).
* `--no-boolean`: Skip boolean-based differential checks.

---

## Example Run

```bash
python sqli_tester.py -u "http://127.0.0.1:5000/search?q=INJECT_HERE"
```

Sample output:

```
[+] Target: http://127.0.0.1:5000/search?q=INJECT_HERE
[i] Baseline status: 200, length: 108

---
[>] Testing payload: '
  status: 500, length: 35
  Verdict: POTENTIAL SQLi or server error

---
[>] Testing payload: ' OR '1'='1
  status: 200, length: 127
  Verdict: POTENTIAL SQLi (boolean-based)
```

---

## Installation

1. Clone or copy the project files.
2. Install dependencies:

```bash
pip install flask requests
```

3. Run the vulnerable app in one terminal:

```bash
python vulnerable_app.py
```

4. Run the tester in another terminal:

```bash
python sqli_tester.py -u "http://127.0.0.1:5000/search?q=INJECT_HERE"
```

---

## Educational Notes

The tool demonstrates three main SQL injection techniques:

1. **Error-based** – relies on visible database error messages.
2. **Boolean-based** – detects logical differences in response between true/false conditions.
3. **Time-based** – detects server delays introduced by injected functions like `SLEEP()`.

SQLite (used in this lab) does not support `SLEEP()`. For time-based injection tests, use MySQL or PostgreSQL in your lab environment.

---

## Disclaimer

This tool is designed strictly for **educational purposes** and should only be used in controlled environments such as DVWA, bWAPP, or your own lab setup.
**Do not use against production systems. Unauthorized testing is illegal.**

