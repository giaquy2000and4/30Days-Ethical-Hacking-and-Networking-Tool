import subprocess
import re

def scan_wifi_windows():
    try:
        result = subprocess.check_output(["netsh", "wlan", "show", "networks", "mode=bssid"],
                                         encoding='utf-8', errors='ignore')
    except subprocess.CalledProcessError:
        print("❌ Không thể thực hiện lệnh netsh. Vui lòng chạy script bằng quyền Admin nếu cần.")
        return

    networks = result.split("\n")
    wifi_list = []
    wifi = {}

    for line in networks:
        line = line.strip()

        ssid_match = re.match(r"SSID\s+\d+\s+:\s(.+)", line)
        if ssid_match:
            if wifi:
                wifi_list.append(wifi)
                wifi = {}
            wifi['SSID'] = ssid_match.group(1)

        signal_match = re.match(r"Signal\s+:\s+(\d+)%", line)
        if signal_match:
            wifi['Signal'] = signal_match.group(1) + "%"

        security_match = re.match(r"Authentication\s+:\s+(.+)", line)
        if security_match:
            wifi['Security'] = security_match.group(1)

        channel_match = re.match(r"Channel\s+:\s+(\d+)", line)
        if channel_match:
            wifi['Channel'] = channel_match.group(1)

        bssid_match = re.match(r"BSSID\s+\d+\s+:\s+([0-9A-Fa-f:-]+)", line)
        if bssid_match:
            wifi['BSSID'] = bssid_match.group(1)

    if wifi:
        wifi_list.append(wifi)

    if not wifi_list:
        print("⚠️ Không tìm thấy mạng Wi-Fi nào.")
        return

    # In bảng kết quả
    print("=" * 72)
    print(f"{'STT':<4} {'SSID':<25} {'Tín hiệu':<10} {'Bảo mật':<20} {'Kênh':<5}")
    print("=" * 72)
    for idx, net in enumerate(wifi_list, 1):
        ssid = net.get('SSID', 'Hidden')
        signal = net.get('Signal', 'N/A')
        security = net.get('Security', 'N/A')
        channel = net.get('Channel', 'N/A')
        print(f"{idx:<4} {ssid:<25} {signal:<10} {security:<20} {channel:<5}")
    print("=" * 72)

if __name__ == "__main__":
    scan_wifi_windows()
