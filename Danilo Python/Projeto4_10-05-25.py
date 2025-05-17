from os import system as limp
limp ("cls")

#Meu
# for i in range(10,101,10):
#     print(f"O numero é {i}")

#Professor

# valor=int(input("Digite um valor: "))

# for i in range(valor+1):
#     if i%10==0 and i>0:
#         print (i)

# texto =None
# for i in range(51):
#         if texto== None:
#                 texto=str(i)
#         else:
#                 texto=(f"{texto};{str(i)}")
       
# print (texto)


# for i in range(51):
#         print(i,end=";")

# nome=input("Digete seu Nome: ")

# for i in nome:
#         print(i, end="")
# print()      
# for i in nome:
#         print(i)

# nome=input("Digete seu Nome: ").lower()

# for i in nome:
#     if i not in ["a", "e", "i", "o", "u"]:
#         print(i, end="")
# print()
# for i in nome:
#     if i in ["a", "e", "i", "o", "u"]:
#         print(i, end="")

#*****************************************************************************
# nome=input("Digete seu Nome: ")

# # for i in nome:
# #     if i.lower() in ["a", "e", "i", "o", "u"]:
# #         print(i, end="")
# # print()
# # for i in nome:
# #     if i.lower() not in ["a", "e", "i", "o", "u"]:
# #         print(i, end="")
# #Jeito novo.
# for i in nome:
#     if i not in "aeiouAEIOU":
#         print(i, end="")


#***********************Exercicio******************************
''' Crie um programa em python que peça ao usuario uma frase
em seguida, utilizando um loop for, percorra cada palavra da frasee realize
a s seguintess operações:

1. Imprima a palavra 
2.Conte e imprima o numero de cvogais (AEIOU) presentes na frase
3.Verifique e imprima se a palavra começa com uma vogal ou uma consoante
'''

frase=input("Digete sua frase: ") #Cada bug que você resolve é um nível a mais no jogo da evolução. Continue codando, errando e vencendo!Cada bug que você resolve é um nível a mais no jogo da evolução. Continue codando, errando e vencendo!

# # Define vogais
# vogais = "aeiouAEIOU"

# # Divide a frase em palavras
# palavras = frase.split()

# # Percorre cada palavra
# for palavra in palavras:
#     print(f"\nPalavra: {palavra}")

#     # Conta vogais na palavra
#     total_vogais = sum(1 for letra in palavra if letra in vogais)
#     print(f"Número de vogais: {total_vogais}")

#     # Verifica a primeira letra
#     primeira_letra = palavra[0]
#     if primeira_letra.lower() in "aeiou":
#         print("Começa com uma **vogal**")
#     elif primeira_letra.isalpha():
#         print("Começa com uma **consoante**")
#     else:
#         print("Começa com um símbolo ou número")
for i in frase:
        if i==" ":
                if i in  "aeiouAEIOU":
                        qt_vogal+=1
                        
                else:
                        print()
        else:
                print(i,end="")

print(frase)
print