import socket


def conecxao_com_cliente(cpf_titular,dado,operacao):
    host = 'localhost'
    port = 8000
    addr = (host, port)
    serv_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #cria o socket
    serv_socket.setsockopt(socket.SOL_SOCK, socket.SOCK_STREAM, 1) #reinicializa o socket
    serv_socket.bind(addr) #define a porta e quais ips podem se conectar com o servidor
    serv_socket.listen(10) #define o limite de conexões
    print('aguardando conexao...')
    con, cliente = serv_socket.accept() #servidor aguardando conexão
    print('conectado')
    print('aguardando mensagem...')

    enviar = '{}/{}/{}'.format(cpf_titular,dado_1,dado_2,dado_3,operacao)

    recebe = con.recv(1024) #define que os pacotes recebidos são de ate 1024 bytes
    con.send(enviar.encode()) 
    saida = recebe.decode()
    serv_socket.close()

    return 