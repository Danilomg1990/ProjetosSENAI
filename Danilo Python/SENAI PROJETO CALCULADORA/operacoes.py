import math 

#P118 - Autor: Cauane "Criação da "
# "Criar função que soma as variaveis"
# Revisor - Nathan
#P126 - Autor:Lucas V
# "Criar função que verifica queoperação o usuario selecionou"
# Revisor - Nathan
def verificar_operacoes(operacao: int, valor1, valor2=0):
       
        if operacao == 1:
            print("Opção Soma Selecionada.")
            valor = soma(valor1, valor2)
            return  valor
        
        elif operacao == 2:
            print("Opção Subtração Selecionada.")
            valor = sub(valor1, valor2)
            return  valor

        elif operacao == 3:
            print("Opção Multiplicação Selecionada.")
            valor = mult(valor1, valor2)
            return  valor

        elif operacao == 4:
            print("Opção Divisão Selecionada.")
            valor = div(valor1, valor2)
            return  valor
        
        elif operacao == 5:
            print("Opção Exponenciação Selecionada.")
            valor = expoente(valor1, valor2)
            return  valor

        elif operacao == 6:
            print("Opção Raiz Selecionada.")
            valor = raiz(valor1, valor2)
            return  valor

        elif operacao == 7:
            print("Opção Seno Selecionada.")
            valor = calcular_seno(valor1)
            return  valor

        elif operacao == 8:
            print("Opção Cosseno Selecionada.")
            valor = calcular_cosseno(valor1)
            return  valor
        
        elif operacao == 9:
            print("Opção Tangente Selecionada.")
            valor = calcular_tangente(valor1)
            return  valor
        

#P101 - Autor: Viviane
# "Criar função que soma as variaveis"
# Revisor - Natha

def soma(numero1,numero2):
    res = numero1 + numero2
    return res

#P102 - Autor: Felipe Sponchiado
# "Criar função que subtrai as variaveis"
# Revisor - André Bononi
def sub( numero1, numero2):
    res = numero1 - numero2
    return res

#P106 - Autor: Vitor M
# "Criar função que eleva a um numero"
# Revisor - André Bononi
def expoente(valor1, valor2):
    res = valor1 ** valor2
    return res

#P105 - Autor: Felipe
# "Criar função que extrai a raiz da variavel"
# Revisor - Nathan
def raiz(valor1, valor2):
    if valor2 == 0:
        return "Erro: divisão por zero"
    res = valor1**(1/valor2)
    return res

#P107 - Autor: Heron
# "Criar função que extrai seno, o cosseno e tangente"
# Revisor - Nathan
def calcular_seno(valor):
    """Calcula o seno de um ângulo em radianos."""
    return math.sin(valor)
def calcular_cosseno(valor):
    """Calcula o cosseno de um ângulo em radianos."""
    return math.cos(valor)
def calcular_tangente(valor):
    """Calcula a tangente de um ângulo em radianos."""
    return math.tan(valor)

#P104 - Autor: Vitor Lucas
# "Criar função que multiplica as variveis"
# Revisor - Nathan
def mult(num1, num2):
    result = num1 * num2
    return result

def div(valor1, valor2):
    if valor2 == 0:
        return "Erro: divisão por zero"
    res = valor1/valor2
    return res