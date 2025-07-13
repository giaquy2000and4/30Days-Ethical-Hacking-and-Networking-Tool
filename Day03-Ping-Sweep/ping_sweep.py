#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Multithreaded Ping Sweep Tool.

Description:
This tool sends ICMP (ping) packets to all IP addresses within a specified
network range (in CIDR format). It uses a thread pool to perform the work
concurrently, which significantly speeds up the scanning process.
IPs that respond to the ping are considered "alive" and are printed to the console.

Usage:
python ping_sweep.py <Network CIDR> [Number of Threads]

Example:
python ping_sweep.py 192.168.1.0/24
python ping_sweep.py 10.0.0.0/22 100
"""

import subprocess
import os
import sys
import ipaddress
import threading
from concurrent.futures import ThreadPoolExecutor, as_completed

# A lock to synchronize printing to the console, preventing race conditions among threads
print_lock = threading.Lock()


def ping_worker(ip_address):
    """
    Worker function that pings a single IP address.
    Returns the IP address if it is alive, otherwise returns None.
    """
    ip_str = str(ip_address)
    try:
        # Build the appropriate ping command based on the operating system
        # - Windows: ping -n 1 -w 1000 (1 packet, 1000ms timeout)
        # - Linux/macOS: ping -c 1 -W 1 (1 packet, 1-second timeout)
        if sys.platform == "win32":
            command = ["ping", "-n", "1", "-w", "1000", ip_str]
        else:
            command = ["ping", "-c", "1", "-W", "1", ip_str]

        # Execute the command and hide its output.
        # subprocess.DEVNULL is used to redirect stdout/stderr to "the void",
        # keeping the console clean.
        result = subprocess.run(command, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL, check=False)

        # Check the return code. 0 typically means success (host is alive).
        if result.returncode == 0:
            with print_lock:
                print(f"[+] {ip_str:<15} - Host is alive")
            return ip_address
    except Exception as e:
        # Print an error if something goes wrong while running the subprocess
        with print_lock:
            print(f"[!] Error pinging {ip_str}: {e}")

    return None


def main():
    """
    The main function that orchestrates the program.
    """
    # --- 1. Handle command-line arguments ---
    if len(sys.argv) < 2:
        print("Invalid syntax!")
        print(f"Usage: python {sys.argv[0]} <Network CIDR> [Number of Threads]")
        print(f"Example: python {sys.argv[0]} 192.168.1.0/24 50")
        sys.exit(1)

    network_cidr = sys.argv[1]

    # Default number of threads is 50, but it's configurable.
    # More threads mean a faster scan but higher resource consumption.
    # For a /24 range (254 hosts), 50-100 threads is reasonable.
    num_threads = 50
    if len(sys.argv) > 2:
        try:
            num_threads = int(sys.argv[2])
        except ValueError:
            print(f"[!] Invalid thread count: '{sys.argv[2]}'. Using default value of {num_threads}.")

    # --- 2. Generate a list of IPs from the CIDR network range ---
    try:
        network = ipaddress.ip_network(network_cidr, strict=False)
        all_hosts = list(network.hosts())
        print(f"\n[INFO] Starting scan on network: {network_cidr} ({len(all_hosts)} hosts)")
        print(f"[INFO] Using {num_threads} worker threads...\n")
    except ValueError:
        print(f"[!] Error: '{network_cidr}' is not a valid CIDR network range.")
        sys.exit(1)

    live_hosts = []

    # --- 3. Use ThreadPoolExecutor to manage the threads ---
    # This is a modern and efficient way to handle multithreading in Python.
    with ThreadPoolExecutor(max_workers=num_threads) as executor:
        # Submit all jobs (pinging each IP) to the pool.
        # executor.submit(function, argument) returns a Future object.
        future_to_ip = {executor.submit(ping_worker, ip): ip for ip in all_hosts}

        # as_completed yields futures as they complete, allowing for real-time
        # processing of results without waiting for all tasks to finish.
        for future in as_completed(future_to_ip):
            result = future.result()
            if result:
                live_hosts.append(result)

    # --- 4. Print the final results ---
    print("\n" + "=" * 40)
    print("      SCAN COMPLETE")
    print("=" * 40)

    if live_hosts:
        # Sort the list of live IPs for readability
        live_hosts.sort()
        print(f"\n[✓] Found {len(live_hosts)} live hosts:")
        for ip in live_hosts:
            print(f"    - {ip}")
    else:
        print("\n[✗] No live hosts found in the network range.")

    print("\n")


if __name__ == "__main__":
    main()