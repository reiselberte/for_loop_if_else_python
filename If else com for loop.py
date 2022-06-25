# for_loop_if_else_python
Como Criar uma situacao usando for loop com if else
#IF, ELSE DENTRO DE UM FOR LOOP
#Programa:
#Enviar um e-mail com detalhes da compra online (Maximo 3 tentantivas) para compras confirmadas.

compra_confirmada = True
dados_compras= 'Compra no valor de R$ 345,50 confirmada'

for enviar in range(3):
    if compra_confirmada:
        print (dados_compras)
        print('Detalhes enviado para seu e-mail')
        break
else:
    print('Falha na compra')