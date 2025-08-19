import socket
import argparse
from concurrent.futures import ThreadPoolExecutor, as_completed
from datetime import datetime
import sys
import io

# Force stdout to UTF-8 (avoid encoding issues on Windows)
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

# Common ports list
COMMON_PORTS = [
    20, 21, 22, 23, 25, 53, 67, 68, 69, 80, 110, 111, 123, 135, 137, 138, 139,
    143, 161, 162, 389, 443, 445, 465, 514, 587, 636, 873, 993, 995, 1080, 1194,
    1352, 1433, 1434, 1521, 1723, 2049, 2082, 2083, 2086, 2087, 3306, 3389, 3690,
    4444, 4672, 5432, 5500, 5631, 5900, 5985, 5986, 6000, 6379, 6660, 6667, 7000,
    8000, 8008, 8080, 8081, 8443, 8888, 9000, 9090, 10000
]

def scan_port(host, port, timeout):
    """Try to connect to a specific port."""
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.settimeout(timeout)
            result = s.connect_ex((host, port))
            return port, (result == 0)
    except Exception:
        return port, False

def main():
    parser = argparse.ArgumentParser(description="Simple Multi-threaded Port Scanner")
    parser.add_argument("-H", "--host", required=True, help="Target host (IP or domain)")
    parser.add_argument("-p", "--ports", nargs="+", type=int, help="List of ports to scan")
    parser.add_argument("-t", "--timeout", type=float, default=1.0, help="Timeout per port (seconds)")
    parser.add_argument("-T", "--threads", type=int, default=100, help="Number of threads")
    parser.add_argument("--only-open", action="store_true", help="Show only open ports")

    args = parser.parse_args()

    try:
        target_ip = socket.gethostbyname(args.host)
    except socket.gaierror:
        print(f"[ERROR] Cannot resolve hostname: {args.host}")
        sys.exit(1)

    ports = args.ports if args.ports else COMMON_PORTS

    print("──────────────────────────────")
    print("       PORT SCANNER")
    print("──────────────────────────────")
    print(f"Target       : {args.host} ({target_ip})")
    print(f"Total ports  : {len(ports)}")
    print(f"Timeout      : {args.timeout:.2f}s")
    print(f"Threads      : {args.threads}")
    print("──────────────────────────────")

    start_time = datetime.now()

    results = []
    with ThreadPoolExecutor(max_workers=args.threads) as executor:
        future_to_port = {executor.submit(scan_port, target_ip, port, args.timeout): port for port in ports}

        for future in as_completed(future_to_port):
            port, is_open = future.result()
            if args.only_open and not is_open:
                continue
            status = "OPEN" if is_open else "CLOSED"
            print(f"Port {port:<5} → {status}")
            results.append((port, is_open))

    end_time = datetime.now()
    duration = (end_time - start_time).total_seconds()

    print("──────────────────────────────")
    print(f"Scan finished in {duration:.2f} seconds")
    print("──────────────────────────────")

if __name__ == "__main__":
    main()
