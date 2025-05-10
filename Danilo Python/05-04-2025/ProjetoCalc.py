from os import system as limp

limp("cls")

selecione = 0

while selecione != '6':  # Verificando se o usuário deseja sair
    valor1 = float(input("Digite o valor 1: "))
    valor2 = float(input("Digite o valor 2: "))
    
    # Inicializando as variáveis de operação
    soma = valor1 + valor2
    sub = valor1 - valor2
    mult = valor1 * valor2
    div = valor1 / valor2 if valor2 != 0 else None  # Evitando divisão por zero
    exp = valor1 ** valor2

    selecione = input("Selecione a operação:\n\n1 - Somar\n2 - Subtrair\n3 - Multiplicar\n4 - Dividir\n5 - Expoenciação\n6 - Sair\n\n")

    # Realizando as operações
    if selecione == '1':
        print("Resultado da soma: ", soma)
    elif selecione == '2':
        print("Resultado da subtração: ", sub)
    elif selecione == '3':
        print("Resultado da multiplicação: ", mult)
    elif selecione == '4':
        if div is not None:  # Verificando se a divisão não foi por zero
            print("Resultado da divisão: ", div)
        else:
            print("Erro! Não é possível dividir por zero.")
    elif selecione == '5':
        print("Resultado da expoenciação: ", exp)
    elif selecione == '6':
        print("Saindo...")
        break  # Sai do loop quando a opção 6 é escolhida
    else:
        print("Opção inválida! Tente novamente.")
    
    # Após cada operação, os valores são resetados para que o usuário insira novos valores
    valor1 = None
    valor2 = None





