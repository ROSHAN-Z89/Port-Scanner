import sys
import socket
import threading

usage = "python3 port_scanner.py TARGET START_PORT END_PORT"

print("-" * 40)
print("Python Simple Port Scanner")
print("-" * 40)

if len(sys.argv) != 4:
    print(usage)
    sys.exit()

try:
    target = socket.gethostbyname(sys.argv[1])
except socket.gaierror:
    print("Name resolution error")
    sys.exit()

start_port = int(sys.argv[2])
end_port = int(sys.argv[3])

print("Scanning target:", target)

def scan_port(port):
    # TCP scan
    try:
        s_tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s_tcp.settimeout(1)
        conn_tcp = s_tcp.connect_ex((target, port))
        if conn_tcp == 0:
            print(f"TCP Port {port} is open")
        s_tcp.close()
    except Exception:
        pass

    # UDP scan
    try:
        s_udp = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s_udp.settimeout(1)
        # Send a small probe
        s_udp.sendto(b"test", (target, port))
        try:
            data, _ = s_udp.recvfrom(1024)
            print(f"UDP Port {port} is open (response received)")
        except socket.timeout:
            # No reply - could be filtered/closed
            pass
        s_udp.close()
    except Exception:
        pass

threads = []

for port in range(start_port, end_port + 1):
    thread = threading.Thread(target=scan_port, args=(port,))
    threads.append(thread)
    thread.start()

for thread in threads:
    thread.join()
