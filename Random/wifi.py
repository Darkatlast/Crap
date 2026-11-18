import socket

hostname = socket.gethostname()
ip_address = socket.gethostbyname(hostname)

print("Your PC hostname:", hostname)
print("Your PC IP Address:", ip_address)
