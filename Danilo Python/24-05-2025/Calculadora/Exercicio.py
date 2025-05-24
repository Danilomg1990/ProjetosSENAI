'''Crie uma função calculadora(num1,num2,operação)que receba dois numeros e uma string de operação("+","-","*" ou "/"). A função deve:
1-ten'''
from os import system as limp
limp('cls')

import Funcoes as calc
while True:
    
    try:
        num1=float(input("Digite o primeiro numero:"))
        num2=float(input("Digite o segundo numero:"))       
        operador=input("Digite a operção +, -, * , / :")    

        if num2==0 and operador=="/":
            print("Erro: Divisão por zero")
            continue
        elif operador not in ("+","-","*","/"):
            print("Erro: Operação inválida")  
            continue
        if operador=="+":
            resultado=calc.soma(num1,num2)
        elif operador=="-":
            resultado=calc.sub(num1,num2)
        elif operador=="*":
            resultado=calc.mult(num1,num2)
        elif operador=="/":
            resultado=calc.div(num1,num2)
        print("Calculo realizado com sucesso!")
        print(f"O resultado é: {resultado}")
        
    except:
        print("Erro: Entrada Numéricas Inválidas.")   