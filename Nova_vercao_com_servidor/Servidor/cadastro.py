#import sqlite3
import mysql.connector as mysql
from Banco import Cliente
from Banco import Historico
from Banco import Banco
from mysql.connector import Error


class Cadastro:
    '''
        O objetivo da class Cadastro conter as contas criadas.
        Todos as informações do objeto são inicializados e deixados vazios até ser adicionado informações.
    '''

    __slots__=['_lista']
    def __init__(self):
        try:
            self._lista=[]
            #self._conta_cache = Banco()
            conexao = mysql.connect(host = 'localhost',db='test_5',user='root')
            cursor = conexao.cursor()

            sql = """CREATE TABLE IF NOT EXISTS usuarios(id INTEGER AUTO_INCREMENT PRIMARY KEY UNIQUE, 
            banco_numero text NOT NULL, banco_titular_nome text NOT NULL, banco_titular_sobrenome text NOT NULL, 
            banco_titular_cpf VARCHAR(32) NOT NULL, banco_saldo text NOT NULL, banco_limite text NOT NULL, 
            banco_historico_transacoes text NOT NULL, banco_senha VARCHAR(32) NOT NULL, banco_historico_data_abertura text NOT NULL);"""

            cursor.execute(sql)

            conexao.commit()
            conexao.close()
        except Error as erro:
            print("Falha ao criar tabela no Mysql: {}".format(erro))


    def sqlite_create(self,banco):
        
        try:
            if(True):

                conexao = mysql.connect(host = 'localhost',db='test_5',user='root')
                cursor = conexao.cursor()


                numero = str(banco.numero)
                nome = str(banco.titular.nome)
                sobrenome = str(banco.titular.sobrenome)
                cpf = str(banco.titular.cpf)
                saldo = str(banco.saldo)
                limite = str(banco.limite)
                senha = str(banco.senha)

                transacoes = banco._historico.transacoes
                print(transacoes)
                data_abertura = str(banco.historico.data_abertura)
                pega=''
                for i in transacoes:
                    if (transacoes!=[]):
                        pega= pega+i+'\n'

                #cursor.execute(sql)
                cursor.execute('INSERT INTO usuarios (banco_numero, banco_titular_nome, banco_titular_sobrenome, banco_titular_cpf, banco_saldo, banco_limite, banco_historico_transacoes, banco_senha , banco_historico_data_abertura) VALUES (%s,%s,%s,%s,%s,%s,%s,MD5(%s),%s)' , (numero,nome,sobrenome,cpf,saldo,limite,pega,senha,data_abertura))

                conexao.commit()
                conexao.close()

                return True
        except Error as erro:
            print("Falha ao criar tabela no Mysql: {}".format(erro))
            return False
        
    def sqlite_read(self,cpf,senha):
        try:
            if(True):
                conexao = mysql.connect(host = 'localhost',db='test_5',user='root')
                cursor = conexao.cursor()

                cursor.execute("SELECT * FROM usuarios WHERE banco_titular_cpf=%s AND banco_senha= MD5('%s')" %(cpf,senha))
                usuario = cursor.fetchall()
                
               
                
                if (usuario!=[]):
                    #print(usuario)
                    cliente_novo = Cliente(usuario[0][2],usuario[0][3],cpf)
                    banco_novo = Banco(int(usuario[0][1]),cliente_novo,float(usuario[0][5]),float(usuario[0][6]),usuario[0][8])
                        
                    usuario[0][7].split('--')
                           
                    banco_novo.historico.transacoes.append (usuario[0][7])
                    banco_novo.historico.data_abertura = usuario[0][9]
                    conexao.commit()
                    conexao.close()
                   
                    return banco_novo

                conexao.commit()
                conexao.close()
                return False

        except Error as erro:
            print("Falha ao ler Banco de dados: {}".format(erro))
            return False
    def sqlite_readSec(self,cpf):
        try:
            if(True):
                conexao = mysql.connect(host = 'localhost',db='test_5',user='root')
                cursor = conexao.cursor()
                cursor.execute('SELECT * FROM usuarios WHERE banco_titular_cpf= %s'%cpf)
                usuario = cursor.fetchall()
                
                if (usuario!=[]):
                    #print(usuario)
                    print(usuario[0])
                    cliente_novo = Cliente(usuario[0][2],usuario[0][3],cpf)
                    banco_novo = Banco(int(usuario[0][1]),cliente_novo,float(usuario[0][5]),float(usuario[0][6]),usuario[0][8])
                        
                    usuario[0][7].split('--')
                           
                    banco_novo.historico.transacoes.append (usuario[0][7])
                    banco_novo.historico.data_abertura = usuario[0][8]
                    conexao.commit()
                    conexao.close()

                    return banco_novo
                
                conexao.commit()
                conexao.close()
                return False

        except Error as erro:
            print("Falha ao ler Banco de dados: {}".format(erro))
            return False

    def sqlite_update(self,banco_atualizado):
        try:    
            if(True):

                conexao = mysql.connect(host = 'localhost',db='test_5',user='root')
                cursor = conexao.cursor()

                pega=banco_atualizado._historico.transacoes
                lista=''
                for i in pega:
                    if i !='[]' and i!='':
                        lista=lista+i

                
                #print(lista)
                cursor.execute('UPDATE usuarios SET banco_saldo = "%s", banco_limite = "%s", banco_historico_transacoes="%s" WHERE banco_titular_cpf = %s' % (str(banco_atualizado.saldo),str(banco_atualizado.limite),lista,banco_atualizado.titular.cpf))
                print('%s , %s , %s, %s' % (banco_atualizado.saldo,banco_atualizado.limite,lista,banco_atualizado.titular.cpf))
                conexao.commit()
                conexao.close()

                return True

        except Error as erro:
            print("Falha ao fazer update no Mysql: {}".format(erro))


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
        confere=self.buscaSecun(pessoa.titular.cpf)
        i=False
        if confere== None:
            self._lista.append(pessoa)
            self.sqlite_create(pessoa)
            i=True
            
        return i

    def busca(self,cpf,senha):
        '''
            Para buscar o objeto do tipo Banco por meio do cpf passado por parametro

            :parametro cpf: inteiro que representa o da conta cadastrada.
            :retorna Retorna a conta que possui o cpf que foi passado por parametro, caso a conta não seja encontrada retornara o valor None.
        '''
        banco=self.sqlite_read(cpf,senha)
        if(banco != False):
            return banco
        return None
    def buscaSecun(self,cpf):
        '''
            Para buscar o objeto do tipo Banco por meio do cpf passado por parametro

            :parametro cpf: inteiro que representa o da conta cadastrada.
            :retorna Retorna a conta que possui o cpf que foi passado por parametro, caso a conta não seja encontrada retornara o valor None.
        '''
        banco=self.sqlite_readSec(cpf)
        if(banco != False):
            return banco
        return None

    def atualizar(self,banco):
        if(self.sqlite_update(banco)):
            return True
        else:
            return False
