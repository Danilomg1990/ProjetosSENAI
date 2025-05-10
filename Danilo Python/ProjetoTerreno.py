from os import system as limp
limp("cls")
# Desenvolva um scrip que calcula a area de um terreno retangular
# Voce inserirá a base e a altura do terreno e voce apresentara ao usuario a area total do terrreno

largura = int(input("Digite a largura do terreno em metro: "))
comprimento=int(input("Digite a comprimento do terreno em metro: "))
print()

# Representação visual do terreno (com base no comprimento)
print("*" * comprimento)  # Linha superior
print(("*" + (" "* (comprimento-2))+ "*\n")*(largura),sep="",end="")  # Linha do meio
print("*" * comprimento)  # Linha inferior