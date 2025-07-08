import socket
import threading
from queue import Queue
import argparse
import time
from colorama import Fore, Style, init
import pyfiglet

# Initialize colorama
init(autoreset=True)

# Default number of threads
DEFAULT_THREADS = 50

# List of common ports and their corresponding services
COMMON_PORTS = {
    20: 'FTP (Data)',
    21: 'FTP (Control)',
    22: 'SSH',
    23: 'Telnet',
    25: 'SMTP',
    53: 'DNS',
    80: 'HTTP',
    110: 'POP3',
    119: 'NNTP',
    123: 'NTP',
    143: 'IMAP',
    161: 'SNMP',
    194: 'IRC',
    443: 'HTTPS',
    445: 'SMB',
    465: 'SMTPS',
    514: 'Syslog',
    587: 'SMTP (TLS)',
    993: 'IMAPS',
    995: 'POP3S',
    1080: 'SOCKS',
    1194: 'OpenVPN',
    1433: 'MSSQL',
    1521: 'Oracle',
    3306: 'MySQL',
    3389: 'RDP',
    5432: 'PostgreSQL',
    5900: 'VNC',
    8080: 'HTTP Proxy',
    8443: 'HTTPS Alternate',
}

# Queue to hold the ports to be scanned
queue = Queue()
open_ports = []
lock = threading.Lock()


def print_banner():
    """Prints the tool's banner."""
    banner = pyfiglet.figlet_format("Py PortScan", font="slant")
    print(f"{Fore.CYAN}{banner}")
    print(f"{Fore.YELLOW}A simple multi-threaded port scanner by BOCCHI89\n")


def scan_port(target_ip):
    """Gets a port from the queue and scans it."""
    while not queue.empty():
        port = queue.get()
        try:
            # Create a new socket
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            # Set a timeout so it doesn't hang for too long
            s.settimeout(0.5)
            # Attempt to connect
            result = s.connect_ex((target_ip, port))
            if result == 0:
                with lock:
                    service = COMMON_PORTS.get(port, 'Unknown')
                    open_ports.append((port, service))
            s.close()
        except (socket.timeout, socket.error):
            pass
        finally:
            queue.task_done()


def parse_ports(port_spec):
    """Parses the input port string (e.g., '1-1024' or '80,443')."""
    ports = set()
    if not port_spec:
        return sorted(COMMON_PORTS.keys())

    try:
        if '-' in port_spec:
            start, end = map(int, port_spec.split('-'))
            if 0 < start <= end <= 65535:
                for port in range(start, end + 1):
                    ports.add(port)
            else:
                raise ValueError("Invalid port range.")
        else:
            for port in port_spec.split(','):
                port_num = int(port.strip())
                if 0 < port_num <= 65535:
                    ports.add(port_num)
                else:
                    raise ValueError(f"Invalid port number: {port_num}")
        return sorted(list(ports))
    except ValueError as e:
        print(f"{Fore.RED}[!] Error: {e}")
        exit(1)


def main():
    print_banner()

    parser = argparse.ArgumentParser(
        description="A multi-threaded Python Port Scanner.",
        formatter_class=argparse.RawTextHelpFormatter
    )
    parser.add_argument("target", help="The IP address or hostname to scan.")
    parser.add_argument(
        "-p", "--ports",
        help="Specify ports to scan. Examples:\n"
             "  -p 1-1024      (scans a range)\n"
             "  -p 80,443,8080 (scans specific ports)\n"
             "(Default: scans common ports)",
        default=None
    )
    parser.add_argument(
        "-t", "--threads",
        type=int,
        default=DEFAULT_THREADS,
        help=f"Number of threads for scanning (default: {DEFAULT_THREADS})."
    )

    args = parser.parse_args()

    try:
        target_ip = socket.gethostbyname(args.target)
    except socket.gaierror:
        print(f"{Fore.RED}[!] Error: Could not resolve hostname '{args.target}'. Please check it.")
        return

    ports_to_scan = parse_ports(args.ports)
    num_threads = args.threads

    print(f"{Style.BRIGHT}Scanning {target_ip}...")
    print(f"Ports to scan: {len(ports_to_scan)}")
    print(f"Threads: {num_threads}\n")

    start_time = time.time()

    # Put the ports into the queue
    for port in ports_to_scan:
        queue.put(port)

    # Create and start the threads
    threads = []
    for _ in range(num_threads):
        thread = threading.Thread(target=scan_port, args=(target_ip,), daemon=True)
        thread.start()
        threads.append(thread)

    # Wait until the queue is empty
    queue.join()

    end_time = time.time()
    duration = end_time - start_time

    print("-" * 50)
    print(f"{Fore.GREEN}{Style.BRIGHT}Scan results for {target_ip}:")

    if open_ports:
        # Sort results by port number
        open_ports.sort(key=lambda x: x[0])
        print(f"{'PORT':<10}{'STATUS':<15}{'SERVICE'}")
        print(f"{'----':<10}{'------':<15}{'-------'}")
        for port, service in open_ports:
            print(f"{Fore.GREEN}{port:<10}{'OPEN':<15}{service}")
    else:
        print(f"{Fore.YELLOW}No open ports found.")

    print("-" * 50)
    print(f"Scan completed in {duration:.2f} seconds.")


if __name__ == "__main__":
    main()