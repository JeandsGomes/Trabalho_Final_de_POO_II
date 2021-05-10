import datetime

class Cliente():

    __slots__ = ['_nome','_sobrenome','_cpf']

    def __init__(self,nome,sobrenome,cpf):
        self._nome = nome
        self._sobrenome = sobrenome
        self._cpf = cpf

    @property
    def nome(self):
        return self._nome
    
    @nome.setter
    def nome(self,nome):
        self._nome = nome

    @property
    def sobrenome(self):
        return self._sobrenome
    
    @sobrenome.setter
    def sobrenome(self,sobrenome):
        self._sobrenome = sobrenome

    @property
    def cpf(self):
        return self._cpf
    
    @cpf.setter
    def cpf(self,cpf):
        self._cpf = cpf



class Historico():

    __slots__ = ['_data_abertura','_transacoes']

    def __init__(self):
        self._data_abertura = datetime.datetime.today()
        self._transacoes = []
    
    @property
    def transacoes(self):
        return self._transacoes

    def imprime(self):
        print("imprime a data de abertura: {}".format(self._data_abertura))
        print("transações: ")
        for operação in self._transacoes:
            print(".",operação)

class Banco():

    _total_contas = 0

    __slots__ = ['_numero','_titular','_saldo','_limite','_historico']

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
        return self._saldo

    @property
    def historico(self):
        return self._historico

    @property
    def numero(self):
        return self._numero

    @numero.setter
    def numero(self,numero):
        self._numero = numero

    @property
    def limite(self):
        return self._limite

    @limite.setter
    def limite(self,valor):
        self._limite = valor

    def depositar(self,valor):
        if (self.saldo+valor > self.limite):
            return False
        else:
            self._saldo += valor
            self._historico.transacoes.append("deposito de {}".format(valor))
            return True
    
    @property
    def titular(self):
        return self._titular

    def sacar(self,valor):
        if(valor < self._saldo):
            self._saldo -= valor
            self._historico.transacoes.append("saque de {}".format(valor))
            return True
        return False

    
    def transferir(self,destino,valor):
        if(self.sacar(valor)):
            destino.depositar(valor)
            self._historico.transacoes[len(self._historico.transacoes)-1] = "transferencia de {} para conta {}".format(valor, destino.numero)
            return True
        return False

    @property
    def extrato(self):
        self._historico.transacoes.append("tirou extrato - saldo de {}".format(self.saldo))
        return "numero: {} \n {}".format(self._numero,self._saldo)

    @staticmethod
    def get_total_contas():
        return Banco._total_contas