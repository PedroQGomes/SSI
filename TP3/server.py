import socket
import sys, select

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((socket.gethostname(), 12345))
print("server iniciado")
s.listen(5)

while True:
    clientsocket, address = s.accept()
    print("Conneçao do cliente aceite")

    print("Introduz o teu codigo - tens 30 segundos")

    i, o, e = select.select( [sys.stdin], [], [], 30 )


    if (i):
        input1 = (f"{sys.stdin.readline().strip()}")
        clientsocket.send(bytes(f"{input1}", "utf-8"))
        print("Dados enviados - Terminar Conneçao")
    else:
        print("Erro: Expiraram os 30 segundos")


    clientsocket.close()
