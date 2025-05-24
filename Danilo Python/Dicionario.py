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

# user={"Nome":input("Insira seu nome: "),
#       "DataNascimento":input("Insira sua data de nascimento: "),
#       "Cpf":int(input("Insira seu CPF: ")),
#       "Telefone":int(input("Insira seu numero de telefone: "))}

# print(f"Meus dados são:\nnome: {user["Nome"]}\nData de nascimento: {user["DataNascimento"]}\
#       \nCPF: {user["Cpf"]}\nTelefone: {user["Telefone"]}")


'''
VOCE VAI DAR UMA FESTA DE ANIVERSARIO
PARA PARTICIPAR DA FESTA, VOCE CONVIDOU 30 PESSOAS

APOS A FESTA, VOCE QUER ENVIAR UM PRESENTE DE OBRIGADO POR PARTICIPAR DA FESTA,
MAS PARA ENVIAR OS PRESENTES VOCE PRECISA TER CERTEZA DE QUEM VEIO NA SUA FESTA 
E QUANTAS PESSOAS ERAM PARA ENCOMENDAR OS PRESENTES NA QUANTIDADE CERTA

DESENVOLVA UM SISTEMA QUE CADA CONVIDADE, AO ENTRAR NA FESTA,
TENHA QUE DIGITAR SEU NOME NUM TECLADO DISPONIVEL NA ENTRADA DA FESTA.

TODOS OS NOMES DOS CONVIDADOS DEVEM SER SALVOS EM UMA LISTA[], TUPLA() OU DICIONARIO{}.

CASO SEJA DIGITADO O CODIGO 12345, O SISTEMA DEVE SER ENCERRADO E APRESENTAR TODOS OS
NOMES DOS USUARIO QUE FORAM À FESTA.

'''
#Minha Aplicação
lista=[]
convidados={}
num=1
while True:
      nome=input("Insira seu nome: ")
      if nome.lower() =="12345": 
            break      
      # lista.append(nome) 
      convidados[num]=nome
      num+=1
print("Os usuarios presentes. Segue a lista!!!!!")
for chave,valor in convidados.items():
      print(f"{chave}-{valor} \U0001F381")  

# print(f"O numero total de presentes são: {len(convidados)}")



#Professor
# senha="12345"
# num=0
# nomes = []
# x=0

# while num<30:
#       conv=input("Digite seu nome: ")
#       num +=1
#       if conv == senha:
#             for i in range(len(nomes)) or num == 30:
#                   print(f"Convidado{x}: {nomes[i]}")
#             break
#       else:
#             nomes.append(conv)
      


