
from Banco import Banco
import socket
from cadastro import Cadastro
from Banco import Cliente
from Banco import Historico
from Banco import Banco

class Servidor():

    def __init__(self):
        self._cadastro = Cadastro()
        self._n_conta = 0

    def mostrar_todas_contas(self):
        for conta in self._cadastro.lista_contas:
            print('{} - {} - {}'.format(conta.titular.cpf,conta.titular.nome,conta.saldo))

    def pre_processamento(self,codigo):

        codigo_lista = codigo.split('/')
        #cadastra
        #cadastrar/nome/sobre_nome/cpf
        if(codigo_lista[0]=='0'):
            codigo_lista[0] = 'cadastra'
        #login
        #login/cpf
        elif(codigo_lista[0]=='1'):
            codigo_lista[0] = 'login'
        #deposita
        #deposito/cpf/valor
        elif(codigo_lista[0]=='2'):
            codigo_lista[0] = 'deposito'
        #saque
        #saque/cpf/valor
        elif(codigo_lista[0]=='3'):
            codigo_lista[0] = 'saque'
        #transferencia
        #transferencia/cpf/valor/cpf_conta_para_transferir
        elif(codigo_lista[0]=='4'):
            codigo_lista[0] = 'transferencia'
        #historico
        #historico/cpf
        elif(codigo_lista[0]=='5'):
            codigo_lista[0] = 'historico'
            
        return codigo_lista

    def cadastrar(self,codigo):
        pessoa = Cliente(codigo[1],codigo[2],codigo[3])
        conta = Banco(self._n_conta,pessoa,0.0,1000)
        self._n_conta =+ 1
        if(self._cadastro.cadastra(conta)):
            return '1'
        return '0' 

    def login(self,codigo):
        conta = self._cadastro.busca(codigo[1])
        if conta != None:
            return '1/{}/{}/{}'.format(conta.titular.nome,conta.titular.sobrenome,conta.saldo)
        return '0'

    def deposito(self,codigo):
        conta = self._cadastro.busca(codigo[1])
        if conta != None:
            if(conta.depositar(float(codigo[2]))):
                return '1/{}'.format(conta.saldo)
            return '0'
        return '0'

    def saque(self,codigo):
        conta = self._cadastro.busca(codigo[1])
        if conta != None:
            if(conta.sacar(float(codigo[2]))):
                return '1/{}'.format(conta.saldo)
            return '0'
        return '0'

    def transferencia(self,codigo):
        conta = self._cadastro.busca(codigo[1])
        conta_1 = self._cadastro.busca(codigo[3])
        if conta != None and conta_1!=None:
            if(conta.transferir(conta_1,float(codigo[2]))):
                return '1/{}'.format(conta.saldo)
            return '0'
        return '0'
    
    def historico(self,codigo):
        conta = self._cadastro.busca(codigo[1])
        if conta != None:
            n_transacoes=len(conta.historico.transacoes)
            if(n_transacoes > 4):
                n_transacoes = 4
            transacoes_str = ''
            for i in range(0,n_transacoes):
                transacoes_str = transacoes_str+'/'+conta.historico.transacoes[i]
            return '1'+transacoes_str
        return '0'

    def ligar_servidor(self):
        host = 'localhost'
        port = 8000
        addr = (host, port)
        serv_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #cria o socket
        serv_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1) #reinicializa o socket
        serv_socket.bind(addr) #define a porta e quais ips podem se conectar com o servidor
        serv_socket.listen(10) #define o limite de conexões


        while(True):
            print('-aguardando conexao...')
            con, cliente = serv_socket.accept() #servidor aguardando conexão
            print('-coneccao realizada')
            
            #operacoes do servidor
            print('-aguardando solicitacao...')
            recebe = con.recv(1024) #define que os pacotes recebidos são de ate 1024 bytes
            
            print('-solicitacao recebida...')

            #pre-processamento do codigo
            codigo = self.pre_processamento(recebe.decode())
            print(codigo)
        
            if(codigo[0] == 'cadastra'):
                saida = self.cadastrar(codigo)
                con.send(saida.encode())
            elif(codigo[0] == 'login'):
                saida = self.login(codigo)
                con.send(saida.encode())
            elif(codigo[0] == 'deposito'):
                saida = self.deposito(codigo)
                con.send(saida.encode())
            elif(codigo[0] == 'saque'):
                saida = self.saque(codigo)
                con.send(saida.encode())
            elif(codigo[0] ==  'transferencia'):
                saida = self.transferencia(codigo)
                con.send(saida.encode())
            elif(codigo[0] == 'historico'):
                saida = self.historico(codigo)
                con.send(saida.encode())

            print('-solicitacao recebida...')
            print('-{} feito por conta {}'.format(codigo[0],codigo[1]))
            print('')
            self.mostrar_todas_contas()
            print('')

            #print('codigo recebido: {}'.format(codigo))

        serv_socket.close()