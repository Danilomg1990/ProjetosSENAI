from os import system as limp
limp ("cls")

i=1
texto= None
while True:
    numero= int(input("Digite um numero inteiro:"))
    if numero%2==0:
        print(f"O numero digitado {numero} é par")
        if texto==None:
            texto=f"{str(numero)}"
            i+=1
        else:
            texto=f"{texto} / {str(numero)}"
            i+=1
    else:
        print(f"O numero digitado {numero} é Impar")
    if i>3:
        print(f"Os numeros pares digitado foi = {texto}\nObrigado por utilizar")
        break