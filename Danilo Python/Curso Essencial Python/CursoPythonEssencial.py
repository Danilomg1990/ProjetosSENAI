from os import system as limp
import AulasSenai as Al  # Certifique-se de que este módulo está disponível

limp('cls')

class CursoPythonEssencial:
    def __init__(self):
        self.aulas = [
            "1 - Introdução ao Python",
            "2 - Tipos de Dados",
            "3 - Estruturas de Controle",
            "4 - Funções",
            "5 - Módulos e Pacotes",
            "6 - Manipulação de Arquivos",
            "7 - Tratamento de Exceções",
            "8 - Programação Orientada a Objetos",
            "9 - Bibliotecas Padrão",
            "10 - Projeto Final",
            "0 - Sair"
        ]

    def listar_aulas(self):
        print("Aulas do Curso Python Essencial:")
        for aula in self.aulas:
            print(aula)

    def chamar_aula(self, numero_aula):
        try:
            numero_aula = int(numero_aula)
            if numero_aula == 0:
                print("\nSaindo do Curso Obrigao!...")
                return False  # sinal para sair
            elif 1 <= numero_aula <= 10:
                print(f"\nVocê escolheu a aula: {self.aulas[numero_aula - 1]}")
                match numero_aula:
                    case 1:
                        Al.Aula01(self.aulas[numero_aula - 1])
                        input("\nPressione Enter para continuar...")
                    case 2:
                        Al.Aula02(self.aulas[numero_aula - 1])
                        input("\nPressione Enter para continuar...")

                    case _:
                        print("Aula ainda não implementada.")
            else:
                print("\nNúmero da aula inválido.")
        except ValueError:
            print("\nPor favor, insira um número válido.")
        return True  # continuar rodando

# Programa principal
curso = CursoPythonEssencial()
continuar = True
while continuar:
    limp('cls')
    curso.listar_aulas()
    escolha = int(input("\nDigite o número da aula que deseja ver: "))
    if escolha < 0 or escolha > 10:
        print("\nNúmero da aula inválido. Tente novamente.")    
    else:
        continuar = curso.chamar_aula(escolha)
        if not continuar:
            break