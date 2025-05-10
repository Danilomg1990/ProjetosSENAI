from os import system as limp
limp ("cls")

# for i in range(10,101,10):
#     print(f"O numero é {i}")

valor=int(input("Digite um valor: "))

for i in range(valor+1):
    if i%10==0 and i>0:
        print (i)


