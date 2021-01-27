import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((socket.gethostname(), 12345))
print("server iniciado")
s.listen(5)

while True:
    clientsocket, address = s.accept()
    print("Conneçao do cliente aceite")

    print("Introduz o teu codigo")
    input1 = (f"{input()}")

    clientsocket.send(bytes(f"{input1}", "utf-8"))
    clientsocket.close()
