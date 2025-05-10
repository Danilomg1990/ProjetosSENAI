from os import system as limp
limp("cls")

texto="""
******************************************************
******************************************************
******************************************************
******************   CAFÉ's SENAI    *****************
******************************************************

ESCOLHA UMA BEBIDA DE ABAIXO:

1 - CAFÉ EXPRESSO","\n2 - CAFÉ COM LEITE","\n3 - CAPPUCCINO\
","\n4 - ÁGUA QUENTE","\n5 - LEITE PURO","\n6 - SAIR"

        ******************************************************
"""
print(texto)
print()
while True:
    try:
        selection = int(input("SELECIONE A OPÇÃO: "))
        if selection == 1:
            print("Você escolheu: CAFÉ EXPRESSO")
            print()
        elif selection == 2:
            print("Você escolheu: CAFÉ COM LEITE")
        elif selection == 3:
            print("Você escolheu: CAPPUCCINO")
            print()
        elif selection == 4:
            print("Você escolheu: ÁGUA QUENTE")
            print()
        elif selection == 5:
            print("Você escolheu: LEITE PURO")
            print()
        elif selection == 6:
            print("Obrigado!")
            print()
            break
        elif selection == 123:
            print("\n1 - TESTE CAFÉ EXPRESSO","\n2 - TESTE CAFÉ COM LEITE","\n3 - TESTE CAPPUCCINO\
                ","\n4 - TESTE ÁGUA QUENTE","\n5 - TESTE LEITE PURO","\n6 - SAIR")
            print()
            try:
                selection1 = int(input("SELECIONE A OPÇÃO: "))
                
                if selection1 == 1:
                    print("Você escolheu:TESTE CAFÉ EXPRESSO")
                    print()
                elif selection1 == 2:
                    print("Você escolheu:TESTE CAFÉ COM LEITE")
                elif selection1 == 3:
                    print("Você escolheu:TESTE CAPPUCCINO")
                    print()
                elif selection1 == 4:
                    print("Você escolheu:TESTE ÁGUA QUENTE")
                    print()
                elif selection1 == 5:
                    print("Você escolheu:TESTE LEITE PURO")
                    print()
                elif selection1 == 6:
                    print("Você escolheu:TESTE FINALIZADO")
                    print()
                    print(texto)
            except ValueError:
                print("Por favor, insira um número válido.")
        else:
            print("Seleção inválida! Por favor, escolha um número entre 1 e 5.")
    except ValueError:
        print("Por favor, insira um número válido.")

# Professor

# limp("cls")

# print(("*" *43 +"\n")*3)
# print("*" * 10, end="")
# print("\tCAFÉ's SENAI\t","*" * 10)
# print("*"*43)
# print("ESCOLHA UMA BEBIDA ABAIXO:\n\n1 - CAFÉ EXPRESSO\n\
# 2 - CAFÉ COM LEITE\n3 - CAPPUCINO\n4 - ÁGUA QUENTE\
# \n5 - LEITE PURO")
# print("*"* 43,"\n\n")
