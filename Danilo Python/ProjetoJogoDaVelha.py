import random

def criar_tabuleiro():
    return [[" " for _ in range(3)] for _ in range(3)]

def imprimir_tabuleiro(tabuleiro):
    print("\n")
    for linha in tabuleiro:
        print(" | ".join(linha))
        print("-" * 5)

def verificar_vitoria(tabuleiro, jogador):
    for i in range(3):
        if all([tabuleiro[i][j] == jogador for j in range(3)]) or \
           all([tabuleiro[j][i] == jogador for j in range(3)]):
            return True
    if all([tabuleiro[i][i] == jogador for i in range(3)]) or \
       all([tabuleiro[i][2 - i] == jogador for i in range(3)]):
        return True
    return False

def verificar_empate(tabuleiro):
    for linha in tabuleiro:
        if " " in linha:
            return False
    return True

def escolher_jogada_bot(tabuleiro):
    # Escolhe aleatoriamente uma posição livre para o bot jogar
    possibilidades = [(i, j) for i in range(3) for j in range(3) if tabuleiro[i][j] == " "]
    return random.choice(possibilidades)

def jogo_da_velha():
    tabuleiro = criar_tabuleiro()
    jogador_atual = "X"  # O jogador humano começa
    jogadas = 0

    print("🎮 Bem-vindo ao Jogo da Velha contra o Bot!")
    imprimir_tabuleiro(tabuleiro)

    while jogadas < 9:
        if jogador_atual == "X":
            try:
                linha = int(input("Escolha a linha (0, 1 ou 2): "))
                coluna = int(input("Escolha a coluna (0, 1 ou 2): "))
            except ValueError:
                print("⚠️ Digite apenas números válidos (0, 1 ou 2)!")
                continue

            if 0 <= linha <= 2 and 0 <= coluna <= 2:
                if tabuleiro[linha][coluna] == " ":
                    tabuleiro[linha][coluna] = "X"
                    jogadas += 1
                    imprimir_tabuleiro(tabuleiro)
                    if verificar_vitoria(tabuleiro, "X"):
                        print("🎉 Você venceu!")
                        return
                    jogador_atual = "O"  # Agora é a vez do bot
                else:
                    print("🚫 Essa posição já está ocupada! Escolha outra.")
            else:
                print("❌ Posição inválida. Use números de 0 a 2.")
        else:
            print("🤖 O bot está jogando...")
            linha, coluna = escolher_jogada_bot(tabuleiro)
            tabuleiro[linha][coluna] = "O"
            jogadas += 1
            imprimir_tabuleiro(tabuleiro)
            if verificar_vitoria(tabuleiro, "O"):
                print("😱 O bot venceu!")
                return
            jogador_atual = "X"  # Agora é a sua vez

        if verificar_empate(tabuleiro):
            print("🤝 Deu velha! Ninguém venceu.")
            return

# Iniciar o jogo
jogo_da_velha()