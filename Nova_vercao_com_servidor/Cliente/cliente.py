

import socket

class plataforma_cliente():
    '''
        O objeto plataforma_cliente contém um cliente.
        Todos as informações do objeto são inicializados e deixados vazios até ser adicionado informações.
    '''

    __slots__ = ['_nome','_sobrenome','_cpf','_saldo','_transacoes']

    def __init__(self):
        self._nome = ''
        self._sobrenome = ''
        self._cpf = ''
        self._saldo = ''
        self._transacoes = []

    @property
    def sobrenome(self):
        '''
            retorna o sobrenome do cliente.
        '''
        return self._sobrenome

    @property
    def cpf(self):
        '''
            retorna o CPF do cliente.
        '''
        return self._cpf

    @property
    def saldo(self):
        '''
            retorna o Saldo do cliente.
        '''
        return self._saldo

    @property
    def transacoes(self):
        '''
            retorna as transações do cliente.
        '''
        return self._transacoes

    @property
    def nome(self):
        '''
            retorna o nome do cliente.
        '''
        return self._nome


    def conecxao_servidor(self,codigo):
        '''
            Para os dados do cliente serem salvos, devera se conectar com o servidor do banco.

            Após se conectar com o servidor será possivel fazer todas as operações disponíveis.

            :parametro codigo: são as informaçoes com alteraçoes na conta de algum cliente no servidor.
            :retorna as informações obtidas no servidor.
        '''
        
        ip = 'localhost'
        port = 8000
        addr = ((ip, port)) #define a tupla de endereco
        client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #AF_INET parametro para informar familia do protocolo
        client_socket.connect(addr) #realizar conexao
        client_socket.send(codigo.encode()) #envia mensagfem
        print('entrada: '+codigo)
        saida = client_socket.recv(1024).decode()
        client_socket.close() #fecha conexao

        return saida

    def cadastro(self,nome,sobrenome,cpf):
        '''
            Para cadastrar uma pessoa é preciso se conectar ao servidor do banco.

            :Parametros nome,sobrenome,CPf: contém as informações da pessoa que deseja ser cliente do banco.
            :tipo nome,sobrenome,CPf: str
            :raise: se a classe retornar false, não foi possivel fazer o cadastro da pessoa no banco.
            :retorna bool. 

        '''
        codigo = '0/'+nome+'/'+sobrenome+'/'+cpf
        try:
            saida = self.conecxao_servidor(codigo)
        except:
            return False
        print(codigo)
        saida_lst = saida.split('/')
        if(saida_lst[0]=='1'):
            return True
        return False
        

    def login(self,cpf):
        '''
            Para um cliente realizar operações em sua conta é preciso realizar o login.

            :Parametro cpf: deve conter a informação de um cliente que deseja fazer login em sua conta existente.
            :Tipo do cpf: str
            :rises:: class return false: se não for possivel se conectar com o servidor do banco.
            :return: bool.
        '''
        codigo = '1/'+cpf
        try:
            saida = self.conecxao_servidor(codigo)
        except:
            return False
        saida_lst = saida.split('/')
        if(saida_lst[0]=='1'):
            self._nome = saida_lst[1]
            self._sobrenome = saida_lst[2]
            self._saldo = saida_lst[3]
            self._cpf = cpf
            return True
        return False
        

    def deposito(self,cpf,valor):
        '''
            Para realizar deposito é preciso se conectar ao servidor.
            :Parametro CPF: deve conter a informação de um cliente já cadastro no servidor.
            :Tipo cpf: str
            :Parametro valor: o valor a ser creditado na conta do cliente. 
            :Tipo valor: Float.
            :rises:: class return false: se não for possivel se conectar com o servidor do banco.
            :return: bool.


        '''
        codigo = '2'+'/'+cpf+'/'+valor
        try:
            saida = self.conecxao_servidor(codigo)
            print('Saida = %s' % (saida))
        except:
            return False
        saida_lst = saida.split('/')
        if(saida_lst[0]=='1'):
            self._saldo = saida_lst[1]
            return True
        return False

    def saque(self,cpf,valor):
        '''
            Para realizar saque é preciso se conectar ao servidor.
            :Parametro CPF: deve conter a informação de um cliente já cadastro no servidor.
            :Parametro valor: o valor a ser debitado na conta do cliente. :Tipo do parametro: Float.
            :rises:: class return false: se não for possivel se conectar com o servidor do banco.
            :return: bool.


        '''
        codigo = '3'+'/'+cpf+'/'+valor
        try:
            saida = self.conecxao_servidor(codigo)
        except:
            return False
        saida_lst = saida.split('/')
        if(saida_lst[0]=='1'):
            self._saldo = saida_lst[1]
            return True
        return False

    def transferencia(self,cpf,valor,cpf_para_transferir):
        '''
            Para realizar transferecia é preciso se conectar ao servidor.
            :Parametro CPF: deve conter a informação de um cliente já cadastro no servidor que irá realizar a transferencia.
            :Parametro cpf_para_transferir: contem a informação de um cliente já cadastro no servidor que irá recebe a transferencia.
            :Parametro valor: o valor a ser creditado na conta do cliente. :Tipo do parametro: Float.
            :rises:: class return false: se não for possivel se conectar com o servidor do banco.
            :return: bool.

        '''
        codigo = '4'+'/'+cpf+'/'+valor+'/'+cpf_para_transferir
        try:
            saida = self.conecxao_servidor(codigo)
        except:
            return False
        saida_lst = saida.split('/')
        if(saida_lst[0]=='1'):
            self._saldo = saida_lst[1]
            return True
        return False

    def historico(self,cpf):
        '''
            Para visualizar o historico de transações é preciso se conectar ao servidor.
            :Parametro CPF: deve conter a informação de um cliente já cadastro no servidor que irá vizualizar suas transaçoes.
            :rises:: class return false: se não for possivel se conectar com o servidor do banco.
            :return: bool.
        ''' 
        codigo = '5'+'/'+cpf
        try:
            saida = self.conecxao_servidor(codigo)
        except:
            return False
        saida_lst = saida.split('/')
        self._transacoes = []
        print(self._cpf)
        print(self._transacoes)
        if(saida_lst[0]=='1'):
            for i in range(1,len(saida_lst)):
                self._transacoes.append(saida_lst[i])
            return True
        return False


