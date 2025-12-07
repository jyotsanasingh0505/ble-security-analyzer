import socket
import threading
from queue import Queue
from rich.console import Console
from rich.table import Table

console = Console()

def scan_port(host, port, timeout=1.0):
    """Return True if port is open on host, else False."""
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.settimeout(timeout)
            result = s.connect_ex((host, port))
            return result == 0
    except Exception:
        return False

def worker(host, q, open_ports, timeout):
    while not q.empty():
        port = q.get()
        if scan_port(host, port, timeout):
            open_ports.append(port)
        q.task_done()

def scan_ports(host, ports=None, threads=100, timeout=0.8):
    """Scan given ports on host. Returns sorted list of open ports."""
    if ports is None:
        # common 1-1024 quick scan by default (you can change)
        ports = list(range(1, 1025))

    q = Queue()
    for p in ports:
        q.put(p)

    open_ports = []
    thread_list = []
    for _ in range(min(threads, q.qsize())):
        t = threading.Thread(target=worker, args=(host, q, open_ports, timeout))
        t.daemon = True
        t.start()
        thread_list.append(t)

    q.join()
    return sorted(set(open_ports))

def pretty_print_results(host, open_ports):
    table = Table(title=f"Open ports on {host}")
    table.add_column("Port", justify="right")
    table.add_column("Service (common)", justify="left")
    common_services = {
        22: "ssh", 80: "http", 443: "https", 21: "ftp", 25: "smtp",
        53: "dns", 110: "pop3", 143: "imap", 3306: "mysql", 8080: "http-alt"
    }
    if not open_ports:
        console.print(f"[green]No open ports found on {host}[/green]")
        return

    for p in open_ports:
        svc = common_services.get(p, "-")
        table.add_row(str(p), svc)
    console.print(table)
