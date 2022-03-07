import socket

HOST = "localhost"
PORT = 3000

socket = socket.socket(socket.AF_INET6, socket.SOCK_STREAM)
socket.connect((HOST, PORT))


socket.send("yooo".encode("utf-8"))
print(socket.recv(1024).decode("utf-8"))
