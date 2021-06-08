import sqlite3
from Banco import Cliente
from Banco import Historico
from Banco import Banco
from cadastro import Cadastro

import datetime



def main():
    cadastro = Cadastro()
    cliente = Cliente('1','1','1')
    banco = Banco(1,cliente,0,1000)

    cadastro.cadastra(banco)

if __name__=="__main__":
    main()


