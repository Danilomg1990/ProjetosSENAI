# from os import system as limp
# limp("cls")

# tabuada=int(input("Digite um numero de 0 a 10:"))
# numero=1

# while numero<=10:
#     resultado=tabuada*numero
#     print(f"{tabuada} x {numero} = {resultado}")
#     numero+=1
from os import system as limp

while True:
    limp("cls")
    try:
        tabuada = int(input("Digite um número de 0 a 100: "))
        if 0 <= tabuada <= 100:
            print(f"\nTabuada do {tabuada}:\n")
            for numero in range(1, 11):
                print(f"{tabuada} x {numero} = {tabuada * numero}")
        else:
            print("Número fora do intervalo permitido (0 a 100).")

    except ValueError:
        print("Por favor, digite um número inteiro válido.")

    repetir = input("\nDeseja ver outra tabuada? (s/n): ").lower()
    if repetir != 's':
        break