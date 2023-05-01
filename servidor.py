'''

Trablho de Redes

Ruan Pablo de Sousa Estácio
Riane Carla Gomes Alvez

'''
import socket

HOST = 'localhost'
POST = 60000
 
def verifica_impa_par(dado):
    dado = dado.decode()
    if len(dado) < 10:
        if int(dado)%2 == 1:
            dado = "IMPAR"
        else:
            dado = "PAR"
    return dado

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((HOST, POST)) 

print("Iniciando...")

while True:
    s.listen() #escutar
    conn, ender = s.accept()

    data = conn.recv(1024)

    dado_tratado = verifica_impa_par(data)
    print(f"----------------------------------------")
    print(F"Mensagem recebida: {dado_tratado}")
    
    conn.sendall(str.encode(dado_tratado))
    print("Resposta retornada!")
    
    conn.close()