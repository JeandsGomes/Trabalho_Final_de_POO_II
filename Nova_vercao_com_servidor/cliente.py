
import socket

class plataforma_cliente():

    __slots__ = ['_nome','_sobrenome','_cpf','_saldo','_transacoes']

    def __init__(self):
        self._nome = ''
        self._sobrenome = ''
        self._cpf = ''
        self._saldo = ''
        self._transacoes = []

    @property
    def sobrenome(self):
        return self._sobrenome

    @property
    def cpf(self):
        return self._cpf

    @property
    def saldo(self):
        return self._saldo

    @property
    def transacoes(self):
        return self._transacoes

    @property
    def nome(self):
        return self._nome


    def conecxao_servidor(self,codigo):

        #ip = input('digite o ip conexao: ')
        ip = 'localhost'
        port = 8000
        addr = ((ip, port)) #define a tupla de endereco

        client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #AF_INET parametro para informar familia do protocolo
        client_socket.connect(addr) #realizar conexao
        #mensagem = input('digite uma mensagem para enviar ao servidor: ')
        client_socket.send(codigo.encode()) #envia mensagfem
        print('entrada: '+codigo)
        saida = client_socket.recv(1024).decode()
        client_socket.close() #fecha conexao

        return saida

    def cadastro(self,nome,sobrenome,cpf):
        codigo = '0/'+nome+'/'+sobrenome+'/'+cpf
        saida = self.conecxao_servidor(codigo)
        print(codigo)
        saida_lst = saida.split('/')
        if(saida_lst[0]=='1'):
            return True
        return False
        

    def login(self,cpf):
        codigo = '1/'+cpf
        saida = self.conecxao_servidor(codigo)
        saida_lst = saida.split('/')
        if(saida_lst[0]=='1'):
            self._nome = saida_lst[1]
            self._sobrenome = saida_lst[2]
            self._saldo = saida_lst[3]
            self._cpf = cpf
            return True
        return False
        

    def deposito(self,cpf,valor):
        codigo = '2'+'/'+cpf+'/'+valor
        saida = self.conecxao_servidor(codigo)
        saida_lst = saida.split('/')
        if(saida_lst[0]=='1'):
            self._saldo = saida_lst[1]
            return True
        return False

    def saque(self,cpf,valor):
        codigo = '3'+'/'+cpf+'/'+valor
        saida = self.conecxao_servidor(codigo)
        saida_lst = saida.split('/')
        if(saida_lst[0]=='1'):
            self._saldo = saida_lst[1]
            return True
        return False

    def transferencia(self,cpf,valor,cpf_para_transferir):
        codigo = '4'+'/'+cpf+'/'+valor+'/'+cpf_para_transferir
        saida = self.conecxao_servidor(codigo)
        saida_lst = saida.split('/')
        if(saida_lst[0]=='1'):
            self._saldo = saida_lst[1]
            return True
        return False

    def historico(self,cpf):
        codigo = '5'+'/'+cpf
        saida = self.conecxao_servidor(codigo)
        saida_lst = saida.split('/')
        self._transacoes = []
        print(self._cpf)
        print(self._transacoes)
        if(saida_lst[0]=='1'):
            for i in range(1,len(saida_lst)):
                self._transacoes.append(saida_lst[i])
            return True
        return False


