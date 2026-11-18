import socket

target = "192.168.1.104"
for port in range(20, 100):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(0.5)
    result = s.connect_ex((target, port))
    if result == 0:
        print(f"Port {port} is OPEN")
    s.close()