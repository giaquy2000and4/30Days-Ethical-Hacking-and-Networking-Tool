import sys
import argparse
# Sử dụng cách import tường minh để tránh xung đột tên
from scapy.layers.inet import IP, ICMP
from scapy.sendrecv import sr1
from scapy.config import conf
import graphviz
import socket

# Tắt chế độ verbose của scapy để màn hình không bị nhiễu
conf.verb = 0


def run_traceroute(target, max_hops=30, timeout=2):
    """
    Thực hiện traceroute đến một target bằng scapy.

    Args:
        target (str): Domain name hoặc địa chỉ IP của đích.
        max_hops (int): Số hop tối đa để thử.
        timeout (int): Thời gian chờ phản hồi cho mỗi hop (giây).

    Returns:
        list: Một danh sách các dictionary, mỗi dict chứa thông tin về một hop.
    """
    try:
        # Lấy địa chỉ IP của target nếu là domain name
        dest_ip = socket.gethostbyname(target)
        print(f"Traceroute to {target} ({dest_ip}), max {max_hops} hops:\n")
    except socket.gaierror:
        print(f"Error: Could not resolve domain name '{target}'")
        return []

    traced_hops = []

    for ttl in range(1, max_hops + 1):
        # Tạo một gói tin ICMP Echo Request với TTL tương ứng
        packet = IP(dst=dest_ip, ttl=ttl) / ICMP()

        # Gửi gói tin và chờ phản hồi đầu tiên (sr1)
        # reply.time là thời gian nhận được gói tin
        # packet.sent_time là thời gian gửi đi
        reply = sr1(packet, timeout=timeout)

        hop_info = {"ttl": ttl, "ip": None, "rtt": None, "is_target": False}

        if reply is None:
            # Không nhận được phản hồi -> Timeout
            print(f"{ttl:2d}  {'*':>15}  Request timed out.")
            hop_info["ip"] = "*"
        else:
            # Tính thời gian Round-Trip-Time (RTT) bằng mili giây
            rtt = (reply.time - packet.sent_time) * 1000
            hop_info["ip"] = reply.src
            hop_info["rtt"] = rtt

            print(f"{ttl:2d}  {reply.src:>15}  {rtt:.2f} ms")

            # Kiểm tra xem đã đến đích chưa
            # reply.type == 0 -> ICMP Echo Reply (đã đến đích)
            if reply.type == 0:
                hop_info["is_target"] = True
                traced_hops.append(hop_info)
                print(f"\nTrace complete.")
                break

        traced_hops.append(hop_info)

    return traced_hops


def draw_route_graph(hops_data, output_filename="traceroute_graph"):
    """
    Vẽ đồ thị tuyến đường từ kết quả traceroute.

    Args:
        hops_data (list): Danh sách các hop từ hàm traceroute.
        output_filename (str): Tên file output (không bao gồm phần mở rộng).
    """
    if not hops_data:
        print("No data to draw the graph.")
        return

    dot = graphviz.Digraph('Traceroute', comment='Network Path')
    dot.attr('node', shape='box', style='rounded,filled', fillcolor='lightblue')
    dot.attr('edge', color='gray')
    dot.attr(rankdir='LR')  # Sắp xếp từ trái qua phải

    # Nút bắt đầu
    source_node = "My Computer"
    dot.node(source_node, style='filled', fillcolor='palegreen')

    last_node_id = source_node

    for hop in hops_data:
        ttl = hop['ttl']
        ip_address = hop['ip']
        rtt = hop['rtt']

        # Tạo ID và label cho node
        node_id = f"hop_{ttl}_{ip_address}"
        if ip_address == "*":
            node_label = f"Hop {ttl}\n* Timeout *"
            dot.node(node_id, node_label, style='filled', fillcolor='lightcoral')
        else:
            node_label = f"Hop {ttl}\n{ip_address}\n{rtt:.2f} ms"
            # Tô màu khác cho nút đích
            if hop.get("is_target"):
                dot.node(node_id, node_label, style='filled', fillcolor='gold')
            else:
                dot.node(node_id, node_label)

        # Vẽ cạnh nối từ nút trước đó đến nút hiện tại
        dot.edge(last_node_id, node_id)
        last_node_id = node_id

    try:
        # Render đồ thị ra file PNG và tự động mở file
        output_path = dot.render(output_filename, format='png', view=True, cleanup=True)
        print(f"\nGraph saved to: {output_path}")
    except graphviz.backend.execute.ExecutableNotFound:
        print("\nERROR: Graphviz executable not found. Failed to render graph.")
        print(
            "Please ensure you have installed the Graphviz software and added its 'bin' directory to the system's PATH.")
        print("Download from: https://graphviz.org/download/")
    except Exception as e:
        print(f"\nError while drawing graph: {e}")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="A traceroute tool using Scapy and Graphviz for visualization.")
    parser.add_argument("target", type=str, help="The destination IP address or domain name.")
    parser.add_argument("--max-hops", type=int, default=30, help="The maximum number of hops.")
    parser.add_argument("--timeout", type=int, default=2, help="Timeout in seconds for each hop.")

    # In thông báo quyền admin
    print("----------------------------------------------------------------")
    print("NOTE: This script requires Administrator/root privileges to run.")
    print("Please run with 'sudo python your_script.py' on Linux/macOS")
    print("or from an Administrator Command Prompt/PowerShell on Windows.")
    print("----------------------------------------------------------------")

    args = parser.parse_args()

    # Chạy traceroute
    hops = run_traceroute(args.target, args.max_hops, args.timeout)

    # Vẽ đồ thị
    if hops:
        draw_route_graph(hops, output_filename=f"traceroute_{args.target}")