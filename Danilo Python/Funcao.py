from os import system as limp 
limp('cls')

def teste():
    print("Minha primeira função!!! \o/")
    return None

def parametro(nome,idade):
    print(f"Você é {nome} e tem {idade} anos.")

print ("Bem vindo as SENAI!!!")
nome = input("Digite sue nome: ")
idade = input("Digite sua idade: ")

teste()

parametro(nome,idade)
