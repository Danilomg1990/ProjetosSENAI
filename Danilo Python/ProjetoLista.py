from os import system as limp 
limp("cls")

valores=[37,48,11,29,100,99]

# for valor in valores:
#     print(valor)

# #Aula Professor
# print(valores[0])
# print(valores[2])
# print(valores[3])
# print(valores[4])
# print(valores[5])

# #Para saber o comprimento da lista
# print(f"A lista contem {len(valores)} itens.")

# teste=valores
# print(teste)
# print(valores)
# del(valores[0])
# print(valores[0])
# print(teste)

# print(hex(id(valores)))#Verifica a memoria alocada
# print(hex(id(teste)))#Verifica a memoria alocada

# while valores:
#     print(f"A lista contem {len(valores)} itens.")
#     del(valores[0])


#para adicionar um item no final da lista 
valores.append("DANILO")
print(valores)
print(f"A lista contem {len(valores)} itens.")

#para adicionar um item a um endereço especificp na lista 
valores.insert(2,"DANILO")
print(valores)
print(f"A lista contem {len(valores)} itens.")

nomes=["Luiz","Gustavo","Vinicius","Heron","Lucas"]

print(nomes)
#classifica em ordem crescente
nomes.sort()
print(nomes)
#classidica em ordem descrecente 
nomes.sort(reverse=True)
print(nomes)

