import datetime

class Cliente():
    '''
        O objeto Cliente possui um cliente.
        :paramentro nome: O paramentro é usado para obter o nome do cliente
        :tipo nome: str
        :paramentro sobrenome: O paramentro é usado para obter o sobrenome do cliente
        :tipo sobrenome: str
        :paramentro cpf: O paramentro é usado para obter o cpf do cliente
        :tipo nome: str
    '''

    __slots__ = ['_nome','_sobrenome','_cpf']

    def __init__(self,nome,sobrenome,cpf):
        self._nome = nome
        self._sobrenome = sobrenome
        self._cpf = cpf

    @property
    def nome(self):
        '''
            retorna o nome
        '''
        return self._nome
    
    @nome.setter
    def nome(self,nome):
        '''
            atribui a informaçao ao nome
        '''
        self._nome = nome

    @property
    def sobrenome(self):
        '''
            retorna o sobrenome
        '''
        return self._sobrenome
    
    @sobrenome.setter
    def sobrenome(self,sobrenome):
        '''
            atribui a informaçao ao sobrenome
        '''
        self._sobrenome = sobrenome

    @property
    def cpf(self):
        '''
            retorna o cpf
        '''
        return self._cpf
    
    @cpf.setter
    def cpf(self,cpf):
        '''
            atribui a informaçao ao cpf
        '''
        self._cpf = cpf



class Historico():

    __slots__ = ['_data_abertura','_transacoes']
    '''
        O objeto Historico possui varias transaçoes de um cliente.
    '''

    def __init__(self):
        hoje=datetime.datetime.today()
        data_abertura = str(hoje).split(' ')
        self._data_abertura = data_abertura[0]
        self._transacoes = []
    
    @property
    def transacoes(self):
        '''
            retorna as transações feitas por um cliente.
        '''
        return self._transacoes

    @transacoes.setter
    def transacoes(self,transacoes_lista):
        self._transacoes = transacoes_lista

    @property
    def data_abertura(self):
        return self._data_abertura

    @data_abertura.setter
    def data_abertura(self,data_abertura_str):
        self._data_abertura = data_abertura_str

    def imprime(self):
        '''
            Exibe todas as transações feitas pelo cliente em sua conta.
        '''
        print("imprime a data de abertura: {}".format(self._data_abertura))
        print("transações: ")
        for operação in self._transacoes:
            print(".",operação)

class Banco():

    _total_contas = 0

    __slots__ = ['_numero','_titular','_saldo','_limite','_historico']
    '''
        O objeto banco possui varias  contas.
        :Parametro numero: O paramentro é usado para informar o numero da conta do cliente.
        :iparam _numero: aqui armazenamos o numero.
        :tipo numero: int
        :Parametro cliente: O paramentro é usado para informar as informações do cliente.
        :iparam _cliente: aqui armazenamos o cliente.
        :tipo clinte: Cliente
        :Parametro saldo: O paramentro é usado para informar o salda da conta do cliente.
        :iparam _saldo: aqui armazenamos o saldo.
        :tipo saldo: float 
        :Parametro limite: O paramentro é usado para informar o limete da conta do cliente.
        :iparam _limite: aqui armazenamos o limite.
        :tipo limite: float
    '''
    def __init__(self,numero,cliente,saldo,limite):
        self._numero = numero
        self._titular = cliente
        self._saldo = saldo
        self._limite = limite
        # como fazer o teste de historico
        self._historico = Historico()
        Banco._total_contas += 1

    @property
    def saldo(self):
        '''
            retorna o saldo da conta.
        '''
        return self._saldo

    @saldo.setter
    def saldo(self,saldo_interio):
        self._saldo = saldo_interio

    @property
    def historico(self):
        '''
            retorna o historico da conta.
        '''
        return self._historico

    @property
    def numero(self):
        '''
            retorna o numero da conta.
        '''
        return self._numero

    @numero.setter
    def numero(self,numero):
        '''
            atribui o numero da conta.
        '''
        self._numero = numero

    @property
    def limite(self):
        '''
            retorna o limite da conta.
        '''
        return self._limite

    @limite.setter
    def limite(self,valor):
        '''
            atribui o limite da conta.
        '''
        self._limite = valor

    def depositar(self,valor):
        '''
            Um valor so pode ser somado ao saldo do cliente se esse valor for maior que 0 e não ultrapassar o limite.
            :Parametro valor: A quantidade a ser somado no saldo
            :tipo valor: float
            :return: bool
        '''
        if (self.saldo+valor > self.limite and valor > 0):
            return False
        else:
            self._saldo += valor
            self._historico.transacoes.append("deposito de {}".format(valor))
            return True
    
    @property
    def titular(self):
        '''
            retorna o titular da conta.
        '''
        return self._titular

    def sacar(self,valor):
        '''
            Um valor só pode ser retirado do saldo se for maior que 0 e o saldo for maior que o valor informado.
            :Parametro valor: A quantidade a ser subtraido no saldo
            :tipo valor: float
            :return: bool
        '''
        if(valor <= self._saldo and valor > 0):
            self._saldo -= valor
            self._historico.transacoes.append("saque de {}".format(valor))
            return True
        return False

    
    def transferir(self,destino,valor):
        '''
            Um valor só pode ser transferido se o saldo do atual cliente possuir saldo.
            :Parametro destino: A conta destino que ira receber a quantia.
            :tipo destino: Banco
            :Parametro valor: A quantidade a ser somado no saldo da conta destino e subrtraido da conta remetente.
            :tipo: float.
            :return:bool.
        '''
        if(self.sacar(valor)):
            destino.depositar(valor)
            self._historico.transacoes[len(self._historico.transacoes)-1] = "transferencia de {} para conta {}".format(valor, destino.numero)
            return True
        return False

    @property
    def extrato(self):
        '''
            retorna uma str com numero da conta e saldo.
        '''
        self._historico.transacoes.append("tirou extrato - saldo de {}".format(self.saldo))
        return "numero: {} \n {}".format(self._numero,self._saldo)

    @staticmethod
    def get_total_contas():
        '''
            retorna o numero de contas cadastradas no banco.
        '''
        return Banco._total_contas

    def mostrar_conta(self):
        print('self.numero == {}'.format(self._numero))
        print('self.titular.nome == {}'.format(self.titular.nome))
        print('self.titular.sobrenome == {}'.format(self.titular.sobrenome))
        print('self.titular.cpf == {}'.format(self.titular.cpf))
        print('self.saldo == {}'.format(self.saldo))
        print('self.Limite == {}'.format(self.limite))
        print('self.histarico.data_abertura == {}'.format(self.historico.transacoes))
        print('self.histarico.transacoes == {}'.format(self.historico.data_abertura))
