from os import system as limp
limp("cls")

import Funcoes as calc
import Menu as men
 
Historico_lista=[]
while True:
    try:
        limp("cls")
        print(men.MenuPrincipal())
        opcao=int(input("Digite a Opção: "))

        if opcao==0:#Sair do Programa
            print("Finalizando sistema da calculadora")
            break
        elif opcao==100:#Exibe o Historico
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
        elif opcao ==101:#Limpar Historio
            Historico_lista=[]
            print()
            print("Dados limpos")
            input("Pressione Enter para continuar...")
        if opcao in [1, 2, 3, 4,5,6,9,10]:   
                 
            x=float(input("Digite o primeiro numero: "))
            y=float(input("Digite o segundo numero: "))

            if opcao ==1:#Soma
                resultado=calc.soma(x,y)
                tipo="soma"
                sinal="+"
    
            elif opcao==2:#Subtração
                resultado=calc.sub(x,y)
                tipo="subtração"
                sinal="-"

            elif opcao==3:#Multiplicação
                resultado=calc.mult(x,y)
                tipo="multiplicação"
                sinal="x"

            elif opcao==4:#Divisão
                resultado=calc.div(x,y)
                tipo="divisão"
                sinal="/"

            elif opcao==5:#Expoenciação
                resultado=calc.potencia(x,y)
                tipo="expoenciação"
                sinal="^"

            elif opcao==6:#Radiciação
                resultado=calc.raiz(x,y)
                tipo="raiz"
                sinal="√"
            
            elif opcao==9:#Divisão inteira
                resultado=calc.divisao_inteira(x,y)
                tipo="divisão Inteira"
                sinal="//"

            elif opcao==10:#Resto
                resultado=calc.resto(x,y)
                tipo="Resto"
                sinal="/"

            print(f"O resultado da {tipo}: {resultado:.2f}")
            Historico_lista.append(f" {x}{sinal}{y} = {resultado:.2f}")
            print()
            input("Pressione Enter para continuar...")

        elif opcao in [7,8]:  
            x=float(input("Digite o numero: "))
            if opcao==7:#Seno
                resultado=calc.seno(x)
                print(f"O resultado da Expoenciação: {resultado:.2f}")
                print()
                Historico_lista.append(f" Sen({x}) = {resultado:.2f}")
                input("Pressione Enter para continuar...")

            elif opcao==8: #Cosseno
                resultado=calc.cosseno(x)
                print(f"O resultado da Expoenciação: {resultado:.2f}")
                print()
                Historico_lista.append(f" Cos({x}) = {resultado:.2f}")
                input("Pressione Enter para continuar...")
            
            elif opcao==11:#Radianos
                resultado=calc.radianos(x)
                print(f"O resultado Radiano: {resultado:.2f}")
                print()
                Historico_lista.append(f" Radiano({x}) = {resultado:.2f}")
                input("Pressione Enter para continuar...")

    except ValueError:
        print("Entrada inválida. Digite um valor numérico.")
        input("Pressione Enter para continuar...")      