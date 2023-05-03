'''

Trablho de Redes

Ruan Pablo de Sousa Estácio
Riane Carla Gomes Alvez

Cliente
'''
import socket
import random
import time

HOST = "127.0.0.1"
PORT = 60000

while True:
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((HOST, PORT))

    numero = str(random.randrange(1, 10**30))
    # caso queira forçar entra na condição para teste (basta descomentar o abaixo)
    # numero = str(random.randrange(1, 11)) 

    print(f"----------------------------------------")
    print(f"Enviando: {numero}")
    codigo = str.encode(numero)
    s.send(codigo)

    data = s.recv(1024)
    print(f'Retorno: {data.decode()} \nFim')

    s.close()
    time.sleep(10)
