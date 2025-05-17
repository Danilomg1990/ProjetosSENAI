from os import system as limp 
limp('cls')

#Aula sobre dicionario
# info={"Nome":"Danilo","DataNasc":"99/99/9999"}
# print(info["Nome"])
# print(info)

# #editar Valor de dicionario

# info["Nome"]="SENAI"
# print(info)

# #Insrir novo valor no dicionario

# info["Cpf"]=123456789
# print(info)

# #Para deletar item no dicionario
# del(info["Nome"])
# print(info)


# nome=input("Insira seu nome: ")
# data_nascimento=input("Insira sua data de nascimento: ")
# cpf=int(input("Insira seu CPF: "))
# telefone=int(input("Insira seu numero de telefone: "))

user={"Nome":input("Insira seu nome: "),
      "DataNascimento":input("Insira sua data de nascimento: "),
      "Cpf":int(input("Insira seu CPF: ")),
      "Telefone":int(input("Insira seu numero de telefone: "))}

print(f"Meus dados são:\nnome: {user["Nome"]}\nData de nascimento: {user["DataNascimento"]}\
      \nCPF: {user["Cpf"]}\nTelefone: {user["Telefone"]}")


