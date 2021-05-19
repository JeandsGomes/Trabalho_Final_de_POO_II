

from unittest import TestCase, main
from Banco import Banco
from Banco import Cliente
from Banco import Historico

class Teste_Banco(TestCase):

#   *Criar uma classe Historico
#       *entrada: nada
#       *import datetime
#       *Inicialização: self.data_abertura>>(datatime.datatime.today()), self.transacoes>>(lista)
#       *saida: 
#   *def imprime(self):
#       *"imprime a data de abertura: {}".format(self.data_abertura)
#       *"transações: "
#       *for com toddas as trnsações
#           *print(".",operação)
#
#   *forma de salvar as transferencias
#       *deposito
#           *"deposito de {}".format(valor)
#       *saca
#           *"saque de {}".format(valor)
#       *extrato
#           *"tirou extrato - saldo de {}".format(self._saldo)
#       *transferir
#           *"transferencia de {} para conta {}".format(valor, destino.numero)

    def teste_Historico_existe(self):
        historico = Historico()

#   Criar uma classe Cliente
#       *entrada: nome, sobrenome, cpf


    def teste_Cliente_existe(self):
        cliente = Cliente('Jeands','Gomes de Sousa',1)



#TESTES DE GET E SET DA CLASSE CLIENTE
#teste_SeExixteFuncaoNomeCliente
    def teste_get_nome_Cliente_exixte(self):
        cliente = Cliente('Jeands','Gomes de Sousa',1)
        cliente.nome
    
    def teste_get_nome_Cliente_da_saida(self):
        valor_entrada = ['Jeands','Gomes de Sousa',1]         
        valor_esperado = 'Jeands'      
        cliente = Cliente(valor_entrada[0],valor_entrada[1],valor_entrada[2])
        self.assertEqual(cliente.nome,valor_esperado)

    def teste_set_nome_Cliente_exixte(self):
        cliente = Cliente('Jeands','Gomes de Sousa',1)
        cliente.nome = 'Aphonso'
    
    def teste_set_nome_Cliente_da_saida(self):
        valor_entrada = ['Jeands','Gomes de Sousa',1]         
        valor_esperado = 'Aphonso'      
        cliente = Cliente(valor_entrada[0],valor_entrada[1],valor_entrada[2])
        cliente.nome = valor_esperado
        self.assertEqual(cliente.nome,valor_esperado)

    def teste_get_sobrenome_Cliente_exixte(self):
        cliente = Cliente('Jeands','Gomes de Sousa',1)
        cliente.sobrenome
    
    def teste_get_sobrenome_Cliente_da_saida(self):
        valor_entrada = ['Jeands','Gomes de Sousa',1]         
        valor_esperado = 'Gomes de Sousa'      
        cliente = Cliente(valor_entrada[0],valor_entrada[1],valor_entrada[2])
        self.assertEqual(cliente.sobrenome,valor_esperado)

    def teste_set_sobrenome_Cliente_exixte(self):
        cliente = Cliente('Jeands','Gomes de Sousa',1)
        cliente.sobrenome = 'Aphonso'
    
    def teste_set_sobrenome_Cliente_da_saida(self):
        valor_entrada = ['Jeands','Gomes de Sousa',1]         
        valor_esperado = 'Aphonso'      
        cliente = Cliente(valor_entrada[0],valor_entrada[1],valor_entrada[2])
        cliente.sobrenome = valor_esperado
        self.assertEqual(cliente.sobrenome,valor_esperado)

    def teste_get_cpf_Cliente_exixte(self):
        cliente = Cliente('Jeands','Gomes de Sousa',1)
        cliente.cpf
    
    def teste_get_cpf_Cliente_da_saida(self):
        valor_entrada = ['Jeands','Gomes de Sousa',1]         
        valor_esperado = 1      
        cliente = Cliente(valor_entrada[0],valor_entrada[1],valor_entrada[2])
        self.assertEqual(cliente.cpf,valor_esperado)

    def teste_set_cpf_Cliente_exixte(self):
        cliente = Cliente('Jeands','Gomes de Sousa',1)
        cliente.cpf = 3
    
    def teste_set_cpf_get_Cliente_da_saida(self):
        valor_entrada = ['Jeands','Gomes de Sousa',1]         
        valor_esperado = 3      
        cliente = Cliente(valor_entrada[0],valor_entrada[1],valor_entrada[2])
        cliente.cpf = valor_esperado
        self.assertEqual(cliente.cpf,valor_esperado)



#Construa a classe Conta com:
#    *Class conta
#    *Os atributos numero,
#    *titular, vai receer uma instancia cliente
#    *saldo e 
#    *limite. dar limite padrão de 1000 rs

    def teste_Banco_existe(self):
        cliente = Cliente('Jeands','Gomes de Sousa',1)
        banco = Banco(1,cliente,201,500)

#TESTES DE GET E SET DA CLASSE BANCO

    def teste_get_numero_Banco_exixte(self):
        cliente = Cliente('Jeands','Gomes de Sousa',1)
        banco = Banco(1,cliente,201,500)
        banco.numero
    
    def teste_get_numero_Banco_da_saida(self):
        cliente = Cliente('Jeands','Gomes de Sousa',1)
        banco = Banco(1,cliente,201,500)
        valor_entrada = [1,cliente,201,500]         
        valor_esperado = 1      
        self.assertEqual(banco.numero,valor_esperado)

    def teste_set_numero_Banco_exixte(self):
        cliente = Cliente('Jeands','Gomes de Sousa',1)
        banco = Banco(1,cliente,201,500)
        banco.numero = 'Aphonso'
    
    def teste_set_numero_Banco_da_saida(self):
        cliente = Cliente('Jeands','Gomes de Sousa',1)         
        banco = Banco(1,cliente,201,500)
        valor_entrada = 2
        valor_esperado = 2      
        banco.numero = valor_esperado
        self.assertEqual(banco.numero,valor_esperado)

    def teste_get_titular_Banco_exixte(self):
        cliente = Cliente('Jeands','Gomes de Sousa',1)
        banco = Banco(1,cliente,201,500)
        banco.titular
    
    def teste_get_titular_Banco_da_saida(self):
        cliente = Cliente('Jeands','Gomes de Sousa',1)
        banco = Banco(1,cliente,201,500)        
        valor_esperado = cliente      
        self.assertEqual(banco.titular,valor_esperado)

    def teste_get_saldo_Banco_exixte(self):
        cliente = Cliente('Jeands','Gomes de Sousa',1)
        banco = Banco(1,cliente,201,500)
        banco.saldo
    
    def teste_get_saldo_Banco_da_saida(self):
        cliente = Cliente('Jeands','Gomes de Sousa',1)
        banco = Banco(1,cliente,201,500)        
        valor_esperado = 201      
        self.assertEqual(banco.saldo,valor_esperado)

    def teste_get_limite_Banco_exixte(self):
        cliente = Cliente('Jeands','Gomes de Sousa',1)
        banco = Banco(1,cliente,201,500)
        banco.limite
    
    def teste_get_limite_Banco_da_saida(self):
        cliente = Cliente('Jeands','Gomes de Sousa',1)
        banco = Banco(1,cliente,201,500)
        valor_entrada = [1,cliente,201,500]         
        valor_esperado = 500      
        self.assertEqual(banco.limite,valor_esperado)

    def teste_set_limite_Banco_exixte(self):
        cliente = Cliente('Jeands','Gomes de Sousa',1)
        banco = Banco(1,cliente,201,500)
        banco.limite = 700
    
    def teste_set_limite_Banco_da_saida(self):
        cliente = Cliente('Jeands','Gomes de Sousa',1)         
        banco = Banco(1,cliente,201,500)
        valor_entrada = 700
        valor_esperado = 700     
        banco.limite = valor_entrada
        self.assertEqual(banco.limite,valor_esperado)



#
#    *Os métodos deposita, 
#        *acrescenta o Valor ao self.saldo

    def teste_deposito_Banco_existe(self):
        cliente = Cliente('Jeands','Gomes de Sousa',1)
        banco = Banco(1,cliente,201,500)
        banco.depositar(20)

    def teste_deposito_Banco_saldo_esperado(self):
        valor_entrada = 20
        valor_esperado = 221
        cliente = Cliente('Jeands','Gomes de Sousa',1)
        banco = Banco(1,cliente,201,500)
        banco.depositar(20)
        self.assertEqual(banco.saldo,valor_esperado)



    def teste_deposito_Banco_imprimir_historico(self):
        valor_entrada = 20
        valor_esperado = ["deposito de {}".format(valor_entrada)]
        cliente = Cliente('Jeands','Gomes de Sousa',1)
        banco = Banco(1,cliente,201,500)
        banco.depositar(20)
        self.assertEqual(banco.historico.transacoes,valor_esperado)


#    
#    *saca e
#        *Decrementa com o Valor o self.saldo 
#       *impedir o saque caso o valor do saldo foir menor retornando False
#       *caso o saque for possivel retornar True

    def teste_sacar_Banco_existe(self):
        cliente = Cliente('Sthefany','Gomes de Sousa',1)
        banco = Banco(1,cliente,201,500)
        banco.sacar(20)

    def teste_saca_Banco_valor_True(self):
        valor_entrada = 20
        valor_esperado = True
        cliente = Cliente('Jeands','Gomes de Sousa',1)
        banco = Banco(1,cliente,201,500)
        self.assertEqual(banco.sacar(20),valor_esperado)

    def teste_saca_Banco_valor_False(self):
        valor_entrada = 20
        valor_esperado = False
        cliente = Cliente('Jeands','Gomes de Sousa',1)
        banco = Banco(1,cliente,19,500)
        self.assertEqual(banco.sacar(20),valor_esperado)

    def teste_saca_Banco_saldo_esperado(self):
        valor_entrada = 20
        valor_esperado = 181
        cliente = Cliente('Jeands','Gomes de Sousa',1)
        banco = Banco(1,cliente,201,500)
        banco.sacar(20)
        self.assertEqual(banco.saldo,valor_esperado)

    def teste_saca_Banco_imprimir_historico(self):
        valor_entrada = 20
        valor_esperado = ["saque de {}".format(valor_entrada)]
        cliente = Cliente('Jeands','Gomes de Sousa',1)
        banco = Banco(1,cliente,201,500)
        banco.sacar(20)
        self.assertEqual(banco.historico.transacoes,valor_esperado)


#    
#    *extrato;
#        *imprime a seguinte informação:
#            *"numero: {} \n {}".format(self.numero, self.saldo)
#    
#    

    def teste_extrato_Banco_existe(self):
        cliente = Cliente('Sthefany','Gomes de Sousa',1)
        banco = Banco(1,cliente,201,500)
        banco.extrato

    def teste_extrato_Banco_valor_esperado(self):
        valor_entrada = 20
        valor_esperado = "numero: {} \n {}".format(1,201)
        cliente = Cliente('Jeands','Gomes de Sousa',1)
        banco = Banco(1,cliente,201,500)
        self.assertEqual(banco.extrato,valor_esperado)

    def teste_extrato_Banco_imprimir_historico(self):
        valor_entrada = 20
        cliente = Cliente('Jeands','Gomes de Sousa',1)
        banco = Banco(1,cliente,201,500)
        banco.extrato
        valor_esperado = ["tirou extrato - saldo de {}".format(banco.saldo)]
        self.assertEqual(banco.historico.transacoes,valor_esperado)

#   *transferir
#       *entrada: destinatario, valor
#       *saida: depositar valor na outra conta
#           *Impeça caso o valor da transferencia for maior que o valor informado


    def teste_transferir_Banco_existe(self):
        cliente_0 = Cliente('Jeands','Gomes de Sousa',1)
        banco_0 = Banco(1,cliente_0,201,500)
        cliente_1 = Cliente('Sthefany','Gomes de Sousa',1)
        banco_1 = Banco(2,cliente_1,200,500)
        banco_0.transferir(banco_1,10)
    
    def teste_trasferir_Banco_True(self):
        valor_entrada = 20
        valor_esperado = True
        cliente = Cliente('Jeands','Gomes de Sousa',1)
        banco_0 = Banco(1,cliente,201,500)
        banco_1 = Banco(1,cliente,201,500)
        self.assertEqual(banco_0.transferir(banco_1,20),valor_esperado)

    def teste_trasferir_Banco_False(self):
        valor_entrada = 20
        valor_esperado = False
        cliente = Cliente('Sthefany','Gomes de Sousa',1)
        banco_0 = Banco(1,cliente,19,500)
        banco_1 = Banco(1,cliente,201,500)
        self.assertEqual(banco_0.transferir(banco_1,20),valor_esperado)


    def teste_trasferir_Banco_valor_esperado(self):
        valor_entrada = 20
        valor_esperado = [181,221]
        cliente = Cliente('Sthefany','Gomes de Sousa',1)
        banco_0 = Banco(1,cliente,201,500)
        banco_1 = Banco(2,cliente,201,500)
        banco_0.transferir(banco_1,20)
        self.assertEqual([banco_0.saldo,banco_1.saldo],valor_esperado)

    def teste_transferir_Banco_imprimir_historico(self):
        valor_entrada = 20  
        cliente = Cliente('Sthefany','Gomes de Sousa',1)
        banco_0 = Banco(1,cliente,201,500)
        banco_1 = Banco(1,cliente,201,500)
        banco_0.transferir(banco_1,20)
        valor_esperado = ["transferencia de {} para conta {}".format(valor_entrada, banco_1.numero)]
        self.assertEqual(banco_0.historico.transacoes,valor_esperado)

#Testes para atributos de classes

    def teste_get_total_contas_existe_Banco_banco_0(self):
       cliente = Cliente('Sthefany','Gomes de Sousa',1)
       banco_0 = Banco(1,cliente,201,500)
       banco_1 = Banco(1,cliente,201,500)
       banco_0.get_total_contas()

#    def teste_get_total_contas_Banco_banco_0_retorn_2(self):  
#        cliente = Cliente('Sthefany','Gomes de Sousa',1)
#        banco_0 = Banco(1,cliente,201,500)
#        banco_1 = Banco(1,cliente,201,500)
#        valor_esperado = 2
#        self.assertEqual(banco_0.get_total_contas(),valor_esperado)

    def teste_get_total_contas_existe_Banco_Banco(self):
        cliente = Cliente('Sthefany','Gomes de Sousa',1)
        banco_0 = Banco(1,cliente,201,500)
        banco_1 = Banco(1,cliente,201,500)
        Banco.get_total_contas()

#    def teste_get_total_contas_Banco_Banco_retorn_2(self):  
#        cliente = Cliente('Sthefany','Gomes de Sousa',1)
#        banco_0 = Banco(1,cliente,201,500)
#        banco_1 = Banco(1,cliente,201,500)
#        valor_esperado = 2
#        self.assertEqual(banco_0.get_total_contas(),valor_esperado)
    
#Como fazer testes com methodos estaticos ??



if __name__ == '__main__':
    main()


