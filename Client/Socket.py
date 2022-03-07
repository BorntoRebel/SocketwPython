import socket


# to dynamically get IP address
# host = socket.gethostbyname(socket.gethostname())

HOST = "localhost"
PORT = 3000

# initialize socket and communication
server = socket.socket(socket.AF_INET6, socket.SOCK_STREAM)
server.bind((HOST, PORT))  # passing a tuple to listen


server.listen(5)

while True:
    communication_socket, address = server.accept()  # comms for the indiviual client.
    print(f"Connect to {address}")
    message = communication_socket.recv(1024).decode("utf-8")
    print(f"Message from client is: {message}")
    communication_socket.send(f"got it".encode("utf-8"))
    communication_socket.close()
    print(f"no longer connected with {address} bye")
