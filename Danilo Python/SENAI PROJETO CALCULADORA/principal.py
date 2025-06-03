#P119 - Autor: Vitor N
# "Criar e preparar novo arquivo princinpal.py"
# Revisor - André

from os import system as limp
import historico as hist
import operacoes as calc
import interface as interface
import game_cobrinha as game

codigo_secreto = 10

nome_operacoes = {
    "1": "Adição",
    "2": "Subtração",
    "3": "Multiplicação",
    "4": "Divisão",
    "5": "Exponenciação",
    "6": "Raiz",
    "7": "Seno",
    "8": "Cosseno",
    "9": "Tangente",
}
simbolos_operacoes = {
    "1": "+",
    "2": "-",
    "3": "*",
    "4": "/",
    "5": "**",
    "6": "raiz",
    "7": "sin",
    "8": "cos",
    "9": "tan",
}

def menu_opcao():
    limp("cls")
    interface.bemvindo()
    while True: 
       interface.Iniciar()
       try:
         operacao = int(input("Selecione uma opção: "))
         break
       except ValueError:
           print("\nValor inválido...\n")
           continue
    return operacao

while True:
    valor1 = 0
    valor2 = 0
    oper= menu_opcao()
    if oper == 0: 
        print("Obrigado por utilizar a calculadora!")
        break
    if oper == codigo_secreto:
        game.iniciar_game()
        continue
    else:
        valor1 = float(input("Digite o primeiro valor: "))
        if oper in (1, 2, 3, 4, 5, 6):
            valor2 = float(input("Digite o segundo valor: "))
            
        resultado = calc.verificar_operacoes(oper, valor1, valor2)
        mensagem = f'Resultado da operação de {nome_operacoes.get(str(oper))} é: {resultado}'
        simbolo = simbolos_operacoes.get(str(oper))
        historico = f'{valor1} {simbolo} {valor2} = {resultado}'
        hist.salvar_historico(historico)
        print(mensagem)
        
    input("Precione Enter para continuar...")
