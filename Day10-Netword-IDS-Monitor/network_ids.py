from scapy.all import sniff, Raw, conf
import smtplib
from email.mime.text import MIMEText

# === CẤU HÌNH CẢNH BÁO ===
KEYWORDS = [b"admin", b"root", b"passwd", b"password"]

EMAIL_FROM = "kocogaming188@gmail.com"  # Email gửi
EMAIL_TO = ["kocogaming188@gmail.com"]  # Danh sách người nhận
EMAIL_USER = "kocogaming188@gmail.com"
EMAIL_PASS = "cgcp ilsl tonf qxza"
EMAIL_SUBJECT = "🔴 Network IDS Alert"
SMTP_SERVER = "smtp.gmail.com"
SMTP_PORT = 587

# === HIỂN THỊ DANH SÁCH INTERFACE DỄ HIỂU ===
def choose_interface():
    iface_list = list(conf.ifaces.values())
    print("🔎 Danh sách interface khả dụng:")
    for idx, iface in enumerate(iface_list):
        name = iface.description or iface.name
        print(f"{idx}. {name}")
    while True:
        try:
            choice = int(input("👉 Nhập số interface muốn chọn: "))
            return iface_list[choice].name  # Trả về tên thô cho sniff()
        except (ValueError, IndexError):
            print("[!] Lựa chọn không hợp lệ. Thử lại.")

# === GỬI EMAIL CẢNH BÁO ===
def send_email_alert(payload):
    try:
        msg = MIMEText(f"Cảnh báo: Phát hiện gói tin đáng ngờ!\n\nPayload:\n{payload}")
        msg["Subject"] = EMAIL_SUBJECT
        msg["From"] = EMAIL_FROM
        msg["To"] = ", ".join(EMAIL_TO)

        with smtplib.SMTP(SMTP_SERVER, SMTP_PORT) as server:
            server.starttls()
            server.login(EMAIL_USER, EMAIL_PASS)
            server.sendmail(EMAIL_FROM, EMAIL_TO, msg.as_string())

        print("[+] Đã gửi cảnh báo qua email.")
    except Exception as e:
        print(f"[!] Lỗi gửi email: {e}")

# === PHÂN TÍCH GÓI TIN ===
def process_packet(packet):
    if packet.haslayer(Raw):
        payload = packet[Raw].load
        for keyword in KEYWORDS:
            if keyword in payload:
                print(f"[!] Phát hiện từ khóa '{keyword.decode()}' trong payload:")
                print(payload)
                send_email_alert(payload)
                break

# === CHẠY CHƯƠNG TRÌNH CHÍNH ===
if __name__ == "__main__":
    iface = choose_interface()
    print(f"[*] Đang theo dõi interface: {iface}")
    sniff(iface=iface, prn=process_packet, store=0)
