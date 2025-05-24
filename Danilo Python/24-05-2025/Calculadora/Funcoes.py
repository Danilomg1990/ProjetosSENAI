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

def potencia(numero1, numero2):
    res = numero1 ** numero2
    return res

def divisao_inteira(numero1, numero2):
    if numero2 == 0:
        return "Erro: divisão por zero"
    
def resto(numero1, numero2):
    if numero2 == 0:
        return "Erro: divisão por zero"
    res = numero1 % numero2
    return res

def raiz(numero1, numero2):
    if numero2 == 0:
        return "Erro: divisão por zero"
    res = numero1**(1/numero2)
    return res

def radianos(numero1):
    return numero1 * (3.141592653589793 / 180)

def fatorial(n):
    # A função fatorial(n) é usada na sua função seno ou cosseno() 
    # para calcular o denominador de cada termo da série de Taylor, 
    # garantindo que o valor do seno seja calculado corretamente usando a fórmula:
    resultado = 1
    for i in range(2, n + 1):
        resultado *= i
    return resultado

def seno(numero1, termos=10):
    x = radianos(numero1)
    seno = 0
    for n in range(termos):
        termo = ((-1) ** n) * (x ** (2 * n + 1)) / fatorial(2 * n + 1)
        seno += termo
    return seno

def cosseno(numero1, termos=10):
    x = radianos(numero1)
    cosseno = 0
    for n in range(termos):
        termo = ((-1) ** n) * (x ** (2 * n)) / fatorial(2 * n)
        cosseno += termo
    return cosseno


