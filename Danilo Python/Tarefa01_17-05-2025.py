from os import system as limp
limp('cls')


# #Primeira forma mais simples
# nome=input("Insira seu nome: ")
# data_nascimento=input("Insira sua data de nascimento: ")
# cpf=input("Insira seu CPF: ")
# telefone=input("Insira seu numero de telefone: ")

# User=[nome,data_nascimento,cpf,telefone]

# print(f"Meus dados são:\nnome: {User[0]}\nData de nascimento : {User[1]}\
#       \nCPF: {User[2]}\nTelefone: {User[3]}")


# #Segunda forma mais simples
# user=[]
# user.append(input("Insira seu nome: "))
# user.append(input("Insira sua data de nascimento: "))
# user.append(input("Insira seu CPF: "))
# user.append(input("Insira seu numero de telefone: "))


# print(f"Meus dados são:\nnome: {user[0]}\nData de nascimento: {user[1]}\
#       \nCPF: {user[2]}\nTelefone: {user[3]}")

# del(user[2])

# print(f"Meus dados são:\nnome: {user[0]}\nData de nascimento: {user[1]}\
#       \nTelefone: {user[2]}\n Cpf deletado com sucesso!")

# #Terceira forma com dicionario
# user = {
#     "nome": input("Insira seu nome: "),
#     "data_nascimento": input("Insira sua data de nascimento: "),
#     "cpf": input("Insira seu CPF: "),
#     "telefone": input("Insira seu número de telefone: ")
# }

# print(f"\nMeus dados são:")
# print(f"Nome: {user['nome']}")
# print(f"Data de nascimento: {user['data_nascimento']}")
# print(f"CPF: {user['cpf']}")
# print(f"Telefone: {user['telefone']}")

#Segunda forma mais simples

nome=input("Insira seu nome: ")
data_nascimento=input("Insira sua data de nascimento: ")
cpf=int(input("Insira seu CPF: "))
telefone=int(input("Insira seu numero de telefone: "))

user=(nome,data_nascimento,cpf,telefone)

print(f"Meus dados são:\nnome: {user[0]}\nData de nascimento: {user[1]}\
      \nCPF: {user[2]}\nTelefone: {user[3]}")







