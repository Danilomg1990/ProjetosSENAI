from os import system as limp
limp("cls")

# nome= "DANILO GUIMARAES"
# print(nome)

# nome= input(Digite seu nome:)
# print(nome)


# nome= input("Digite seu nome:")
# print(nome)

# for letra in nome:
#     print(letra)

# data=int(input("Digite o ano que você nasceu: "))
# idade = 2025 - data
# print("Sua idade é:", idade, "anos.")

# SOLICITAR AO USUARIO QUE INSIRA OS SEGUINTES DADOS NA TELA DO SISTEMA
# NOME: DEVE SER UMA STRING 
# DATA NASCIMENTO: DEVE SER UMA STRING
# CPF:DEVE SER UMA INT
# TELEFONE: DEVE SER UMA INT

# GERAR UMA FUNÇÃO PRINT QUE TRAGA TODAS AS SUAS INFORMAÇÕES DE FORMA ORGANIZADA

nome = input("Digite seu nome:")
data = input("Digite sua data de nascimento:")
cpf = int(input("Digite seu CPF:"))
fone = int(input("Digite seu Telefone:"))

print()
print("MEUS DADOS SÃO:\nNOME:",nome,"\nDATA DE NASCIMENTO",data,"\nCPF:",cpf,"\nTELEFONE:",fone,sep="")

