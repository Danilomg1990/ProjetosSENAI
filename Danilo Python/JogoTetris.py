import pygame
import random

# Inicializar o Pygame
pygame.init()

# Cores
BRANCO = (255, 255, 255)
AZUL = (0, 0, 255)
VERDE = (0, 255, 0)
VERMELHO = (255, 0, 0)
AMARELO = (255, 255, 0)
ROXO = (128, 0, 128)
CINZA = (30, 30, 30)

cores = [AZUL, VERDE, VERMELHO, AMARELO, ROXO]

# Tela
LARGURA_TELA = 300
ALTURA_TELA = 600
TAMANHO_BLOCO = 30
LINHAS = ALTURA_TELA // TAMANHO_BLOCO
COLUNAS = LARGURA_TELA // TAMANHO_BLOCO
TELA = pygame.display.set_mode((LARGURA_TELA, ALTURA_TELA))
pygame.display.set_caption("Tetris")

# Formas
formas = [
    [[1, 1, 1, 1]],  # I
    [[1, 1], [1, 1]],  # O
    [[1, 1, 0], [0, 1, 1]],  # S
    [[0, 1, 1], [1, 1, 0]],  # Z
    [[1, 0, 0], [1, 1, 1]],  # L
    [[0, 0, 1], [1, 1, 1]],  # J
    [[0, 1, 0], [1, 1, 1]]   # T
]

def criar_peca():
    forma = random.choice(formas)
    cor = random.choice(cores)
    return {'forma': forma, 'cor': cor, 'x': COLUNAS // 2 - len(forma[0]) // 2, 'y': 0}

def desenhar_tela():
    TELA.fill(CINZA)
    for y in range(LINHAS):
        for x in range(COLUNAS):
            pygame.draw.rect(TELA, BRANCO, (x * TAMANHO_BLOCO, y * TAMANHO_BLOCO, TAMANHO_BLOCO, TAMANHO_BLOCO), 1)

def desenhar_peca(peca):
    for y, linha in enumerate(peca['forma']):
        for x, valor in enumerate(linha):
            if valor:
                pygame.draw.rect(
                    TELA,
                    peca['cor'],
                    ((peca['x'] + x) * TAMANHO_BLOCO, (peca['y'] + y) * TAMANHO_BLOCO, TAMANHO_BLOCO, TAMANHO_BLOCO)
                )

def mover_peca(peca, dx, dy):
    peca['x'] += dx
    peca['y'] += dy

def girar_peca(peca):
    peca['forma'] = [list(linha) for linha in zip(*peca['forma'][::-1])]

def verificar_colisao(peca, tabuleiro):
    for y, linha in enumerate(peca['forma']):
        for x, valor in enumerate(linha):
            if valor:
                px = peca['x'] + x
                py = peca['y'] + y
                if px < 0 or px >= COLUNAS or py >= LINHAS:
                    return True
                if py >= 0 and tabuleiro[py][px]:
                    return True
    return False

def fixar_peca(peca, tabuleiro):
    for y, linha in enumerate(peca['forma']):
        for x, valor in enumerate(linha):
            if valor:
                tabuleiro[peca['y'] + y][peca['x'] + x] = peca['cor']

def remover_linhas(tabuleiro):
    linhas_removidas = 0
    for i in range(LINHAS - 1, -1, -1):
        if all(tabuleiro[i]):
            del tabuleiro[i]
            tabuleiro.insert(0, [None] * COLUNAS)
            linhas_removidas += 1
    return linhas_removidas

# Loop principal
def jogo():
    clock = pygame.time.Clock()
    tabuleiro = [[None] * COLUNAS for _ in range(LINHAS)]
    peca_atual = criar_peca()
    tempo_queda = 0
    intervalo_queda = 500  # milissegundos
    running = True

    while running:
        tempo_passado = clock.tick(60)
        tempo_queda += tempo_passado

        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                running = False
            elif evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_LEFT:
                    mover_peca(peca_atual, -1, 0)
                    if verificar_colisao(peca_atual, tabuleiro):
                        mover_peca(peca_atual, 1, 0)
                elif evento.key == pygame.K_RIGHT:
                    mover_peca(peca_atual, 1, 0)
                    if verificar_colisao(peca_atual, tabuleiro):
                        mover_peca(peca_atual, -1, 0)
                elif evento.key == pygame.K_DOWN:
                    mover_peca(peca_atual, 0, 1)
                    if verificar_colisao(peca_atual, tabuleiro):
                        mover_peca(peca_atual, 0, -1)
                        fixar_peca(peca_atual, tabuleiro)
                        remover_linhas(tabuleiro)
                        peca_atual = criar_peca()
                        if verificar_colisao(peca_atual, tabuleiro):
                            running = False
                elif evento.key == pygame.K_UP:
                    girar_peca(peca_atual)
                    if verificar_colisao(peca_atual, tabuleiro):
                        for _ in range(3):  # gira de volta
                            girar_peca(peca_atual)

        # Queda automática
        if tempo_queda > intervalo_queda:
            mover_peca(peca_atual, 0, 1)
            if verificar_colisao(peca_atual, tabuleiro):
                mover_peca(peca_atual, 0, -1)
                fixar_peca(peca_atual, tabuleiro)
                remover_linhas(tabuleiro)
                peca_atual = criar_peca()
                if verificar_colisao(peca_atual, tabuleiro):
                    running = False
            tempo_queda = 0

        # Desenho
        desenhar_tela()
        desenhar_peca(peca_atual)
        for y, linha in enumerate(tabuleiro):
            for x, cor in enumerate(linha):
                if cor:
                    pygame.draw.rect(
                        TELA,
                        cor,
                        (x * TAMANHO_BLOCO, y * TAMANHO_BLOCO, TAMANHO_BLOCO, TAMANHO_BLOCO)
                    )

        pygame.display.update()

    pygame.quit()

# Rodar o jogo
if __name__ == "__main__":
    jogo()