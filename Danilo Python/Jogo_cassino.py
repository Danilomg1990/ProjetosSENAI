import random
import time
from os import system as limp

# Lista de símbolos do caça-níquel
simbolos = ['🍒', '🔔', '🍋', '💎', '7️⃣']

def puxar_alavanca():
    limp('cls')  # Limpa a tela (apenas no Windows)
    print("🎰 Girando...")
    time.sleep(1)

    # Sorteia 3 símbolos
    slot = [random.choice(simbolos) for _ in range(3)]
    
    # Mostra os símbolos
    print(f"| {' | '.join(slot)} |")
    
    # Verifica se o jogador ganhou
    if slot[0] == slot[1] == slot[2]:
        print("💰 JACKPOT! Você ganhou!")
    elif slot[0] == slot[1] or slot[1] == slot[2] or slot[0] == slot[2]:
        print("✨ Quase lá! Dois símbolos iguais!")
    else:
        print("😢 Nada feito. Tente novamente!")

# Loop principal
while True:
    input("\nPressione Enter para puxar a alavanca...")
    puxar_alavanca()

    jogar_novamente = input("\nDeseja jogar novamente? (s/n): ").lower()
    if jogar_novamente != 's':
        print("🎲 Obrigado por jogar! Até a próxima!")
        break
    