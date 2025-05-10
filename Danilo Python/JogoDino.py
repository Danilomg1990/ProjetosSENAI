import pygame
import random  # Adicionado para usar random

# Inicializar o Pygame
pygame.init()

# Definindo as cores
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREEN = (34, 139, 34)

# Definindo o tamanho da tela
WIDTH = 800
HEIGHT = 400
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Dino Game')

# Definir o FPS
clock = pygame.time.Clock()
FPS = 60

# Definir o Dino (personagem)
dino_width = 50
dino_height = 50
dino_x = 50
dino_y = HEIGHT - dino_height - 10
dino_velocity_y = 0
gravity = 0.8
jump_strength = -12
is_jumping = False

# Definir obstáculos
obstacle_width = 20
obstacle_height = 50
obstacle_velocity = 5
obstacles = []

# Pontuação
score = 0
font = pygame.font.SysFont('arial', 30)

# Função para desenhar o Dino
def draw_dino(x, y):
    pygame.draw.rect(screen, GREEN, (x, y, dino_width, dino_height))

# Função para desenhar os obstáculos
def draw_obstacles(obstacles):
    for obs in obstacles:
        pygame.draw.rect(screen, BLACK, (obs[0], obs[1], obstacle_width, obs[2]))

# Função para gerar obstáculos
def generate_obstacle():
    height = random.randint(30, 50)
    x_position = WIDTH
    y_position = HEIGHT - height - 10
    return [x_position, y_position, height]

# Função para detectar colisão
def check_collision(dino_rect, obstacles):
    for obs in obstacles:
        obstacle_rect = pygame.Rect(obs[0], obs[1], obstacle_width, obs[2])
        if dino_rect.colliderect(obstacle_rect):
            return True
    return False

# Função principal do jogo
def game():
    global dino_y, dino_velocity_y, is_jumping, score, obstacles  # Declarando obstacles como global
    running = True

    while running:
        screen.fill(WHITE)

        # Verificar os eventos (teclas pressionadas, fechar janela)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE and not is_jumping:
                    is_jumping = True
                    dino_velocity_y = jump_strength

        # Física do pulo
        if is_jumping:
            dino_velocity_y += gravity
            dino_y += dino_velocity_y
            if dino_y >= HEIGHT - dino_height - 10:
                dino_y = HEIGHT - dino_height - 10
                is_jumping = False
                dino_velocity_y = 0

        # Gerar obstáculos
        if random.random() < 0.02:
            obstacles.append(generate_obstacle())

        # Mover os obstáculos
        for obs in obstacles:
            obs[0] -= obstacle_velocity

        # Remover obstáculos que saíram da tela
        obstacles = [obs for obs in obstacles if obs[0] + obstacle_width > 0]

        # Desenhar o Dino e os obstáculos
        draw_dino(dino_x, dino_y)
        draw_obstacles(obstacles)

        # Atualizar a pontuação
        score += 1

        # Verificar colisão
        dino_rect = pygame.Rect(dino_x, dino_y, dino_width, dino_height)
        if check_collision(dino_rect, obstacles):
            running = False

        # Exibir a pontuação
        score_text = font.render(f"Score: {score}", True, BLACK)
        screen.blit(score_text, (WIDTH - 150, 20))

        # Atualizar a tela
        pygame.display.update()

        # Definir a taxa de FPS
        clock.tick(FPS)

    # Tela de Game Over
    game_over_text = font.render(f"Game Over! Score: {score}", True, BLACK)
    screen.blit(game_over_text, (WIDTH // 3, HEIGHT // 2))
    pygame.display.update()
    pygame.time.delay(2000)  # Espera 2 segundos antes de fechar

    pygame.quit()

# Iniciar o jogo
if __name__ == "__main__":
    game()
