from os import system as limp
limp("cls")

# x=-2000

# if x>0 :
#     print("O valor é maior que zero")
#     print("O valor é maior que zero")
#     print("O valor é maior que zero")

# print ("Fim de programa")
# print ("Fim de programa")



'''
LÓGICA PARA TOMADAS DE DECISÃO
!= VERIFICA SE É DIFERENTE
>=VERIFICA SE É MAIOR OU IGUAL 
>VERIFICA SE É MAIOR
<=VERIFICA SE É MENOR OU IGUAL
,VERIFICA SE É MENOR

= afirmo que é iguel
== TESTA SE REALMENTE É =

RESPOSTA SERÁ SEMPRE TRUE OR FALSE

'''
# AULA 
# valor = 10
# print(valor == 0)
# print(valor != 0)
# print(valor >=0)
# print(valor > 0)
# print(valor <= 0)
# print(valor < 0)


# valor1 = input("Digite o 1 valor:")
# valor2=input("Digite o 2 valor:")

# print(valor1 == valor2)
# print(valor1 != valor2)
# print(valor1 >=valor2)
# print(valor1 > valor2)
# print(valor1 <= valor2)
# print(valor1 < valor2)


'''
INSIRA UM PROGRMA QUE LEIA UM NUMERO DIGITADO PELO USUARIO E DIGA SE ELE 
É POSITIVO, NEGATIVO OU ZeroDivisionError
'''

# valor=float(input("Digite o valor a ser veriifcado:").replace(",","."))
# texto="O valor digitado é"

# if valor>0:
#     print(texto, "Positivo")
# elif valor < 0:
#     print("",texto, "Negativo")
# else:
#     print(texto, "Zero")

'''
ESCREVA UM PROGRAM QUE SIMULE O ACESSO A UM SISTEMA
O USUARIO DEVE DIGITAR UMA SENHA. SE A SENHA FOR "PYTHON123",
O SISTEMA DEVE MOSTRAR "ACESSO PERMITIDO", SENÃO DEVE MOSTRA 
"SENHA INCORRETA
'''
print("-"*50)
print("-"*50)
print("Verificador de senha:")
print("-"*50)

senha=str(input("Digite a senha:"))

if senha == "PYTHON123":
    print("Acesso Permitido.")
else: 
   print("Acesso não Permitido.")      
