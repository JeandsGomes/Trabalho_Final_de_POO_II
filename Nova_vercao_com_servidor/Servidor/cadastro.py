class Cadastro:
    __slots__=['_lista']
    def __init__(self):
        self._lista=[]

    @property
    def lista_contas(self):
        return self._lista
    
    def cadastra(self,pessoa):
        confere=self.busca(pessoa.titular.cpf)
        i=False
        if confere== None:
            self._lista.append(pessoa)
            i=True
        return i

    def busca(self,cpf):
        confere=None
        for x in self._lista:
            if x.titular.cpf==cpf:
                confere=x
                break
        return confere
