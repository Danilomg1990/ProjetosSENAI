from os import system as limp
limp("cls")

# def teste()
#     print("Minha primeira função!!! \o/")
#     return None

# def par(nome,idade)
#     print (f"Você é o {nome} e tem {idade} anos.")

# print ("Bem vindo ao SENAI")

# par("Danilo,34")

def soma(numero1, numero2):
        res=numero1+numero2
        return res

def sub(numero1, numero2):
        res=numero1-numero2
        return res

def mult(numero1, numero2):
        res=numero1*numero2
        return res

def div(numero1, numero2):
        res=numero1/numero2
        return res

print("Bem vindo à calculadora SENAI. \
Insira os números que quer calcular.")

x=float(input("Digite o primeiro numero: "))
y=float(input("Digite o segundo numero: "))

valor=[]
valor.append=soma(x,y) 
valor.append=sub(x,y) 
valor.append=mult(x,y) 
valor.append=div(x,y) 

print(f"O resultado é:\nSoma: {valor[0]}\nSubtração: {valor[1]}\
      \nMultiplicação: {valor[2]} \nDivisão: {valor[3]:.2f}")




