#P119 - Autor: Vitor N
# "Criar e preparar novo arquivo princinpal.py"
# Revisor - André


#P115 - Autor: Vitor N
# "Desenvolvimento interface boas vindas"
# Revisor - André
from os import system as limp
import historico as historico
import operacoes as calc
import interface as interface
limp("cls")

def menu_opcao():
    interface.bemvindo()
    while True: 
       interface.Iniciar()
       try:
         operacao = int(input("Selecione uma opção: "))
         break
       except ValueError:
           print("Valor inválido...")
           continue
    return operacao
while True:
    oper= menu_opcao()
    valor1 = float(input("Digite o primeiro valor: "))
    if oper in (1, 2, 3, 4, 5):
        valor2 = float(input("Digite o segundo valor: "))
    elif oper == 0:
        print("Obrigado por utilizar a calculadora!")
        break

    resutado=calc.verificar_operacoes(oper, valor1, valor2)


















