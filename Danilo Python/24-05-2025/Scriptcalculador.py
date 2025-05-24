from os import system as limp

limp("cls")

def MenuPrincipal():
    tela_inicial='''************* CALCULADORA SENAI ****************\
        \n\nSelecione a função abaixo:\n\
        \n1- SOMA:\
        \n2- SUBTRAÇÂO:\
        \n3- MULTIPLICAÇÂO:\
        \n4- DIVISÃO:\
        \n5- EXIBIR HISTORICO:\
        \n6- SAIR: \n'''
    return(tela_inicial)

def soma(numero1, numero2):
        reultado=numero1+numero2
        return reultado

def sub(numero1, numero2):
        reultado=numero1-numero2
        return reultado

def mult(numero1, numero2):
        reultado=numero1*numero2
        return reultado

def div(numero1, numero2):
        reultado=numero1/numero2
        return reultado

Historico_lista=[]
while True:
    limp("cls")
    print(MenuPrincipal())
    opcao=int(input("Digite a Opção: "))
    if opcao==6:
        print("Finalizando sistema da calculadora")
        break
    elif opcao==5:
        if len(Historico_lista)==0:
            print()
            print("Não possui Historico!!")
            input("Pressione Enter para continuar...")
            continue
        else:
            n=1
            for item in Historico_lista:
                print(f"{n}-{item}")
                n+=1
            print()
            input("Pressione Enter para continuar...")
        
    if opcao in [1, 2, 3, 4]:            
        x=float(input("Digite o primeiro numero: "))
        y=float(input("Digite o segundo numero: "))

    if opcao ==1:
        resultado=soma(x,y)
        print(f"O resultado da soma: {resultado:.2f}")
        Historico_lista.append(f" {x}+{y} = {resultado:.2f}")
        print()
        input("Pressione Enter para continuar...")
        
    elif opcao==2:
        resultado=sub(x,y)
        print(f"O resultado da subtração: {resultado:.2f}")
        print()
        Historico_lista.append(f" {x}-{y} = {resultado:.2f}")
        input("Pressione Enter para continuar...")

    elif opcao==3:
        resultado=mult(x,y)
        print(f"O resultado da multiplicação: {resultado:.2f}")
        print()
        Historico_lista.append(f" {x}/{y} = {resultado:.2f}")
        input("Pressione Enter para continuar...")

    elif opcao==4:
        resultado=div(x,y)
        print(f"O resultado da divisão: {resultado:.2f}")
        print()
        Historico_lista.append(f" {x}+{y} = {resultado:.2f}")
        input("Pressione Enter para continuar...")


             
    







# print("Bem vindo à calculadora SENAI. \
# Insira os números que quer calcular.")

# x=float(input("Digite o primeiro numero: "))
# y=float(input("Digite o segundo numero: "))

# valor=[]
# valor.append=soma(x,y) 
# valor.append=sub(x,y) 
# valor.append=mult(x,y) 
# valor.append=div(x,y) 

# print(f"O resultado é:\nSoma: {valor[0]}\nSubtração: {valor[1]}\
#       \nMultiplicação: {valor[2]} \nDivisão: {valor[3]:.2f}")