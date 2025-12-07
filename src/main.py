# at top of main.py, add imports
from port_scanner import scan_ports, pretty_print_results

# add a simple runner block (below your current logic)
if __name__ == "__main__":
    # existing BLE demo code...
    # After it, run a quick port scan demo:
    host = input("Enter hostname or IP for quick port scan (or press enter to skip): ").strip()
    if host:
        console.print(f"Scanning {host} (common ports 1-1024)... This can take a bit.")
        open_ports = scan_ports(host, ports=list(range(1, 1025)), threads=200, timeout=0.5)
        pretty_print_results(host, open_ports)
