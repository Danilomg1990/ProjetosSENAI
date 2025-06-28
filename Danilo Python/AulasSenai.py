
def Aula01(aula):
    data_aula="14/06/2025"

    def Aula01_01(data_aula):#Aula introdutoria ao Python
        
        Hora_aula="15:00"
        texto="Nesta aula, se apresentamos para turma, conhecemos sobre python\n\
    e suas principais características, além de aprender a instalar o Python e configurar o ambiente de desenvolvimento.\n\
    Python é uma linguagem de programação de alto nível, interpretada e de tipagem dinâmica.\n"
        print(texto)
        print(f"Data da Aula: {data_aula} {Hora_aula}\n")
        pass
    
    def Aula01_02(data_aula):#Aula para aprender a usar o print
        ''' Função para apresentar a hora da aula.'''
        Hora_aula="15:40"
        ''' Função para limpar a tela do terminal.'''
        # from os import system as limp 
        # limp('cls')
        ''' Função para imprimir uma mensagem..'''
        print("SENAI NA VEIA")
        print("Danilo")
        print("da Matta")
        print("Guimarães")

        #As linhas abaixo imprimem meu nome com end
        print("Danilo", end=" ")
        print("da Matta", end=" ")
        print("Guimarães", end=" ")

        #As linhas abaixo usam o print com /n
        print("Danilo\nda Matta\nGuimarães")

        #Imprimir na tela as suas informações
        print("Nome: Danilo da Matta Guimarães")
        print("Telefone: (11) 99999-9999")
        print("Endereço: Rua Exemplo, 123, São Paulo, SP")
        print("Data de Nascimento: 01/01/1990")
        print("Nacionalidade: Brasileiro")
        print("Naturalidade: Brasileiro")

        print(f"Aula 01 - Introdução ao Python\nData: {data_aula} Hora: {Hora_aula}\n")  
        pass

    def Aula01_03(data_aula):#Aula para aprender a usar o print
        # ''' Função para apresentar a hora da aula.'''
        Hora_aula="16:30"
        #\n - salta para proxima linha
        #\t - tabula o texto
        #\\ - imprime uma barra invertida
        #\' - imprime uma aspa simples
        #\" - imprime uma aspa dupla
        #\ - imprime uma barra normal
        #\b - volta um espaço "backspace"
        #\0 - caractere nulo
        #\r - retorna o cursor para o inicio da linha
        #\U - imprime um caractere unicode
        #\N - imprime um caractere unicode com nome
        #\U0001F600 - imprime um emoji de rosto sorridente
        # #\N{GRINNING FACE} - imprime um emoji de rosto sorridente com nome
        # #\x - imprime um caractere hexadecimal
        # #\o - imprime um caractere octal
        # #\a - toca um beep
        # #\v - salta para a proxima linha vertical
        # # #\f - salta para a proxima pagina
        # # #\c - imprime um caractere de controle
        # # # #\e - imprime um caractere de escape
        # # # # #\x1b - imprime um caractere de escape hexadecimal
        print("#\a")

        # As linhas abaixo usam print com sep
        print("SENAI", "NA", "VEIA", sep="-")
        pass

    def Aula01_04():#Pergunta que cai na prova
        ''' Função para apresentar a hora da aula.'''
        Hora_aula="16:47"
        #Pergunta 1: Qual é o resultado do programa a seguir?
        print("Meu\nnome\né\nBond.", end=" ")
        print("James Bond.")

        #Pergunta 2: Qual é a saída do seguinte programa?
        #print(sep="&", "peixe", "salgadinhos")
        '''O Sep que é usado somente no final'''
        print("peixe", "salgadinhos", sep="&")


        #Pergunta 3: Qual das seguintes invocações da função print() causará um SyntaxError?
        print('Greg\'s book.')
        print("'Greg's book.'")
        print('"Greg\'s book."')
        print("Greg\'s book.")
        # print('"Greg's book."'
        pass

    Aula01_01(data_aula)
    Aula01_02(data_aula)
    Aula01_03(data_aula)
    
def Aula02(aula):
    data_aula="28/06/2025"

    def Aula02_01(data_aula):#Aula para aprender a usar o print
        Hora_aula="08:30"
        texto="Nesta aula, damos continuidade ao print\n\
    aprendemos a criar variaveis como nome idade e depois ao imprimir possa fazer a mudança.\n"
        print(texto)
        print(f"Data da Aula: {data_aula} {Hora_aula}\n")
        print(f"Aula 02 - Tipos de Dados\nData: {data_aula} Hora: {Hora_aula}\n")

        # inicio da Aula 
        nome ="Danilo"
        idade = 35

        print("Meu nome é", nome, "e tenho", idade, "anos.")
        print("Meu nome é Danilo Guimarães e tenho 35 anos.")
        print("E eu \"gosto\" muito de comer sushi.")
        print('E eu "não gosto" de comer churrasco.')

        # Escrever tudo em uma linha de Python
        print("Meu nome é", nome, "e tenho", idade, "anos.")
        print("E eu \"gosto\" muito de comer sushi.")
        print('E eu "não gosto" de comer churrasco.')
        print('Meu nome é', nome, 'e tenho', idade, 'anos.\nEu \
             "gosto" muito de comer sushi.\nE eu "não gosto" de comer churrasco.')
        
        print(10*'#',"teste Cisco Capitulo 2.1",10*'#')
        print("Meu\nnome\né\nBond.", end=" ")
        print("James Bond.")
        # Fim da Aula do print Capitulo 2.1 do Cad Cisco
        print(f"Aula 02 - Tipos de Dados\nData: {data_aula} Hora: {Hora_aula}\n")

    def Aula02_02(data_aula):#Aula para aprender tipos de variaveis
        Hora_aula="09:26"
        texto="Nesta aula, aprendemos sobre os tipos de variaveis\n\
    e como podemos usar elas para armazenar dados.\n\
    Os tipos de variaveis mais comuns são: int, float, str e bool.\n"
        print(texto)

        print(f"Aula 02 - Tipos de Variaveis\nData: {data_aula} Hora: {Hora_aula}\n")

        # Exemplos de variaveis
        nome = "Danilo"
        idade = 35
        altura = 1.75
        estudante = True

        print(f"Nome: {nome} | Idade: {idade} | Altura: {altura} | Estudante: {estudante}")

        # Tipos de variaveis
        print(f"Tipo de {nome}: {type(nome)}")
        print(f"Tipo de {idade}: {type(idade)}")
        print(f"Tipo de {altura}: {type(altura)}")
        print(f"Tipo de {estudante}: {type(estudante)}")

    def Aula02_03(data_aula):#Aula para aprender tipos de variaveis
        Hora_aula="09:58"
        print(f"Aula 02 - Tipos de Variaveis\nData: {data_aula} Hora: {Hora_aula}\n")
        print("Aula após intervalo aprendendo as ter o mesmo numero \
        para Numeros inteiros")
        
        #Numeros inteiros
        numero1 = 20500000
        numero2 = 20_500_000
        numero3 = -20500000
        numero4 = -20_500_000


        # Numero hexadecimal
        numero_hexadecimal = 0x1A3F  # Hexadecimal
        print(f"Numero 1: {numero1} | Tipo: {type(numero1)}")
        print(f"Numero 2: {numero2} | Tipo: {type(numero2)}")
        print(f"Numero 3: {numero3} | Tipo: {type(numero3)}")
        print(f"Numero 4: {numero4} | Tipo: {type(numero4)}")
        print(f"Numero Hexadecimal: {numero_hexadecimal} | Tipo: {type(numero_hexadecimal)}")

        # Numeros octais
        numero_octais = 0o755  # Octal
        print(f"Numero Octal: {numero_octais} | Tipo: {type(numero_octais)}")


    
    Aula02_01(data_aula)
    Aula02_02(data_aula)
    Aula02_03(data_aula)