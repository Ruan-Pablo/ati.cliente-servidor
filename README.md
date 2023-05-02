# Sockets.cliente-servidor
Trabalho feito na linguagem Python para trabalho da disciplina Rede de computadores.
Nos códigos presentes no repositório forão desenvolvidas duas aplicações, uma cliente que se conecta com o servidor e outra servidor. <br> 
-> O <b>programa cliente,</b> é um loop que primeiro ele se conecta ao servidor, gera um número inteiro com 30 casas envia esse número para o servidor. Depois espera a resposta do servidor, recebe a resposta, imprime com "FIM", fecha a conexão e espera 10 segundos até para poder recomeçar o loop. <br>
-> O <b>programa servidor</b> vai esperar a conexão do cliente e quando receber um número, se tiver mais de 10 casas irá gerar e enviar uma string do mesmo tamanho, se for menor que 10, irá verificar se o o número é "impar" ou "par" e retornar essa sentença.<br>  
 
 ## Os Sockets
 Um socket é uma interface que serve para a comunicação entre diferentes computadores conectados a internet, dessa forma é possivel enviar e receber dados através dela. A composição de um socket consiste em:
 <ul>
 <li> Endereço IP </li>
 <li> Número de porta </li>
 </ul> 
 Juntas essas informações identificam um unico processo numa rede, por exemplo, quando um queremos fazer duas máquinas se comunicarem, criamos um socket que contenha o endereço IP e a porta do processo de destino e enviamos dados através desse socket. 
 Existem vários tipos de de sockets, incluindo TCP(é um protocolo orientado a conexão que garante que os dados cheguem ao destino sem perda) e UDP (um protocolo sem conexão que não garante a entrega de dados), neste trabalho foi realizada uma comunicação TCP.
 
 
 
