
# Port Scanner

A simple multithreaded port scanner written in Python.  
This tool allows you to scan common ports on a given target (IP address or domain).  
It provides a command-line interface (CLI) with clean and readable output.

---

## Features

- Scan **common ports** (20, 21, 22, 23, 25, 53, 80, 110, 135, 139, 143, 443, 445, 993, 995, 1723, 3306, 3389, 5900, 8080, etc.).
- Accepts **domain names** or **IP addresses**.
- **Multithreaded scanning** for high performance.
- Configurable **timeout** and **number of threads**.
- Option to **show only open ports**.
- Clean and professional **CLI output**.

---

## Requirements

- Python **3.7+**

No external libraries are required. Uses only the Python standard library.

---

## Installation

Clone or download this repository:

```bash
git clone https://github.com/yourusername/port-scanner.git
cd port-scanner
````

---

## Usage

Run the script from the command line:

```bash
python port_scanner.py -H <target> [options]
```

### Arguments

| Argument          | Description                                 | Default  |
| ----------------- | ------------------------------------------- | -------- |
| `-H`, `--host`    | Target host (IP or domain)                  | Required |
| `-t`, `--threads` | Number of threads to use                    | `200`    |
| `--timeout`       | Timeout per connection attempt (in seconds) | `0.8`    |
| `--only-open`     | Show only open ports                        | Disabled |

---

### Examples

1. Scan a domain with default settings:

   ```bash
   python port_scanner.py -H example.com
   ```

2. Scan with 100 threads and custom timeout:

   ```bash
   python port_scanner.py -H 192.168.1.1 -t 100 --timeout 1.5
   ```

3. Show only open ports:

   ```bash
   python port_scanner.py -H qldaotao.utehy.edu.vn --only-open
   ```

---

## Example Output

```text
──────────────────────────────
  PORT SCANNER
──────────────────────────────
Target      : qldaotao.utehy.edu.vn
Total ports : 72
Timeout     : 0.80s
Threads     : 200

──────────────────────────────
  RESULTS
──────────────────────────────
[+] 22/tcp   OPEN   (SSH)
[+] 80/tcp   OPEN   (HTTP)
[+] 443/tcp  OPEN   (HTTPS)

──────────────────────────────
Scan completed in 2.34s
──────────────────────────────
```

---

## Disclaimer

This tool is created for **educational and research purposes only**.
Do not use it on networks or systems without explicit authorization.
The author is not responsible for any misuse.

---

