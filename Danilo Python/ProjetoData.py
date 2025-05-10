from os import system as limp
from datetime import datetime
limp("cls")

import datetime
# CRIAR UM SISTEMA QUE SOLICITE AO USUARIO QUE INSIRA SEUS DADOS:
# NOME:
# MES DE NASCIMENTO
# ANO DE NASCIMENTO
#IMPRIMIR A SEGUINTE INFORMÇÕES APÓS O USUARIO INSERIR SEUS DADOS:
# Bem vindo <nome> ao SENAI 
#Sua data de nascimento é <dia> / <mes> / <ano>.

nome = input("Digite seu nome:")

dia = int(input("Digite o dia do seu nascimento:"))
mes = int(input("Digite o mes do seu nascimento:"))
ano = int(input("Digite o ano do seu nascimento:"))

tempo=datetime.date.today().strftime("%d/%m/%Y")


print(tempo)

idade=datetime.datetime.now().year - ano

print("Bem vindo ", nome, " ao SENAI!!\n\
Sua data de nascimento é ",dia,"/",mes,"/",ano,sep=""  )
print("Sua idade é de:", idade, end=" anos")

# Soluição do professor
print(f"Bem vindo {nome} ao SENAI!!!",end="")
print(f"Sua data de nascimento é {dia}/{mes}/{ano}.")
