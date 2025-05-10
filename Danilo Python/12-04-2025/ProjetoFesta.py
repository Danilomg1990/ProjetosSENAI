from os import system as limp
from datetime import datetime
limp("cls")
'''
DESAFIO 
DESENVOLVA EM PYTHON UM SCRYPT QUE SOLICITE AO USUARIO 
QUE INSIRA O SEU ANO DE NASCIMENTO

SE ESSE USUARIO FOR MAIOR DE IDADE,
ELE PODE ENTRAR NA FESTA.

SE NÃO DOR  MAIOR DE IDADE, ELE NÃO PODE ENTRAR.

APRESENTAR ESSA INFORMAÇÃO AO USUARIO COM O PRINT
'''
print("*"*50)
nascimento = int(input("Insira o ano do seu nascimento:"))
print("*"*50)
hoje=datetime.now().year
idade=hoje-nascimento



if idade>=18:
    print("Bem vindo a festa sinta-se a vontade!")
else:
    print("Você não tem idade para entrar na festa\n\
    Por gentileza poderia se retira.")

