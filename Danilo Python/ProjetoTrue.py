from os import system as limp

limp("cls")

# x=0
# y=0

# print(x==0)
# print(y==0)
# print(x==0 and y==00)
# print()


'''
eSCREVA UM PROGRAMA PARA LER 2 VALORES E ESCREVER O MAIOR DELES

CASO OS VALORES INFORMADO SEJAM IGUAIS, INFORMAR AO USUÁRIO QUE NÃO PODEM SER IGUAIS
'''

# valor1= float(input("Digite o primeiro valor:").replace(",","."))
# valor2= float(input("Digite o segundo valor:").replace(",","."))

# if valor1>valor2:
#     print(f"O Primeiro valor é maior {valor1}")
# elif valor1<valor2:
#     print(f"O Segundo valor é maior {valor2}") 
# else:
#     print("Os valores não podem serem iguais!")
# PEÇA A IDADE DO USUARIO E DIGA EM QUAL GRUPO ELE SE ENCAIX:
#        . CRIANÇA : ATÉ 12
#        . ADOLECENTE: DE 13 A 17 ANOS 
#        . ADULTO: DE 18 A 59 ANOS 
#        . IDOSO: 60 ANOS OU MAIS

# idade= int(input("Digite sua Idade:"))
# if idade<=12:
#     print(f"Você é uma criança com {idade} ",end=" anos")
# elif idade<=17:
#     print(f"Você é um adolecente com {idade}",end=" anos")
# elif idade<=59:
#     print(f"Você é um adulto com {idade}",end=" anos")
# else:
#     print(f"Você é um idoso com {idade}",end=" anos")


# def classificar_idade(idade):
#     if idade <= 12:
#         return f"Você esta no grupo de criança com {idade} anos."
#     elif idade <= 17:
#         return f"Você esta no grupo de adolescente com {idade} anos."
#     elif idade <= 59:
#         return f"Você esta no grupo de adulto com {idade} anos."
#     else:
#         return f"Você esta no grupo de idoso com {idade} anos."

# # Solicitar a idade ao usuário
# while True:
#     try:
#         idade = int(input("Digite sua idade: "))
#         if idade < 0:
#             print("Idade não pode ser negativa!")
#         else:
#             print(classificar_idade(idade))
#             break
#     except ValueError:
#         print("Por favor, digite um número válido para a idade.")


'''
CRIE UM SCRIPT EM PYTHON QUE SOLICITE A NOTA FINAL E A FREQUANCIA
(%) DO ALUNO.

UM ALUNO SERÁ APROVADO SE:

A NOTA FOR MAIOR OU IGUAL A 7 E A FREQUECIA FOR MAIOR OU IGUAL A 75%

'''
# while True:
#     nota= float(input("Digite a nota:").replace(",","."))
#     if nota>10:
#         print("Verifique a nota! Nota maxima 10")
#     elif nota<0:
#         print("Verifique a nota! Nota minima 0")
#     else:
#         break
# while True:
#     frequencia=float(input("Digite a frequencia:").replace(",","."))
#     if  frequencia>100:
#         print("Verifique a frequecia! Frequecia maxima 100")
#     elif frequencia<0:
#         print("Verifique a frequecia! Frequecia minima 0")
#     else:
#         break

# if nota<=10 and frequencia <=100:
#     if nota>= 7 and frequencia >= 75:
#         print("Aluno aprovado!")
#     else:
#         print("Aluno reprovado!")


'''
DESENVOLVA EM PYTHON UM SCRIPT QUE SOLICITE AO USUARIO QUE INSIRAR SUAS INFORMAÇÃO
-PRESSÃO
-TEMPERATURA
- BATIMENTO CARDIACO POR MINUTO

COM BASE NOS DADOS INFORMADOS, O PROGRAMA DEVE ANALISAR
CADA UMA DESSAS INFORMAÇÕES SEPARADAMENTE PARA CLASSIFICAR A CONDIÇÃO DO USUARIO EM

TEMPERATURA CORPORAL:

HIPOTERMIA (ABAIXO DE 35°)
'''

# Entradas
nome = input("Digite o nome do paciente: ")
pressao = float(input("Digite a pressão do paciente: ").replace(",", "."))
temperatura = float(input("Digite a temperatura do paciente (em °C): ").replace(",", "."))
batimento = float(input("Digite o batimento cardíaco do paciente (em bpm): ").replace(",", "."))

# Avaliação da pressão
if pressao < 10.1:
    dados_pressao="BAIXA" 
elif pressao < 14:
    dados_pressao="NORMAL" 
else:
    dados_pressao="ALTA"
texto_pressao = f"Referente à pressão do paciente: {dados_pressao} ({pressao} mmHg)"

# Avaliação da temperatura
if temperatura < 35:
     dados_temperatura="HIPOTERMIA"
elif temperatura <= 37.5:
    dados_temperatura="NORMAL"
elif temperatura <= 39:
    dados_temperatura="FEBRE LEVE"
else:
    dados_temperatura="FEBRE ALTA"
texto_temp = f"Referente à temperatura do paciente: {dados_temperatura} ({temperatura}°C)"

# Avaliação dos batimentos
if batimento < 60:
    dados_bpm="BRAQUICARDIA"
elif batimento > 100:
    dados_bpm="TAQUICARDIA"
else:
    dados_bpm="NORMAL"
texto_bpm = f"Referente ao batimento cardíaco: BRAQUICARDIA ({batimento} bpm)"

#Classificação do Atendimento

if (dados_temperatura=="NORMAL" or dados_temperatura=="FREBE LEVE") and  dados_bpm=="NORMAL" and  dados_pressao=="NORMAL":
    atendimento="ATENDIMENTO NORMAL"
elif dados_temperatura=="FEBRE ALTA" and  dados_bpm=="TAQUICARDIA" and  dados_pressao=="ALTA":
    atendimento="ATENDIMENTO GRAVE"
elif dados_temperatura=="HIPOTERMIA" and  dados_bpm=="BRAQUICARDIA" and  dados_pressao=="BAIXA":
    atendimento="ATENDIMENTO URGENTE"

# Exibição dos resultados
print("\n--- Avaliação do Paciente ---")
print(f"Nome:{nome}")
print(texto_pressao)
print(texto_temp)
print(texto_bpm)
print(atendimento)
