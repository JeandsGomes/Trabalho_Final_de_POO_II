class Cadastro:
    '''
        O objetivo da class Cadastro conter as contas criadas.
        Todos as informações do objeto são inicializados e deixados vazios até ser adicionado informações.
    '''

    __slots__=['_lista']
    def __init__(self):
        self._lista=[]

    @property
    def lista_contas(self):
        '''
            retorna a lista de conta cadastradas.
        '''
        return self._lista
    
    def cadastra(self,pessoa):
        '''
            Para as cadastrar as contontas é passado por parametros um objeto Banco

            :parametro pessoa: objeto de class Banco.
            :retorna True casoa  conta for cadastrada e False caso a conta não seja cadastrada.
        '''
        confere=self.busca(pessoa.titular.cpf)
        i=False
        if confere== None:
            self._lista.append(pessoa)
            i=True
        return i

    def busca(self,cpf):
        '''
            Para buscar o objeto do tipo Banco por meio do cpf passado por parametro

            :parametro cpf: inteiro que representa o da conta cadastrada.
            :retorna Retorna a conta que possui o cpf que foi passado por parametro, caso a conta não seja encontrada retornara o valor None.
        '''
        confere=None
        for x in self._lista:
            if x.titular.cpf==cpf:
                confere=x
                break
        return confere
