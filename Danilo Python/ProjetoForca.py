import random

def escolher_palavra():
    palavras = ["python", "programar", "algoritmo", "forca", "desenvolvedor", "computador"]
    return random.choice(palavras).upper()

def exibir_palavra(palavra_secreta, letras_certas):
    return " ".join([letra if letra in letras_certas else "_" for letra in palavra_secreta])

def forca():
    palavra = escolher_palavra()
    letras_certas = set()
    letras_erradas = set()
    tentativas = 6

    print("🎮 Bem-vindo ao Jogo da Forca!")
    print("_ " * len(palavra))

    while tentativas > 0:
        print("\nPalavra: ", exibir_palavra(palavra, letras_certas))
        print(f"❌ Letras erradas: {' '.join(letras_erradas)}")
        print(f"❤️ Tentativas restantes: {tentativas}")

        tentativa = input("Digite uma letra: ").strip().upper()

        if not tentativa.isalpha() or len(tentativa) != 1:
            print("⚠️ Digite apenas UMA letra válida!")
            continue

        if tentativa in letras_certas or tentativa in letras_erradas:
            print("⛔ Você já tentou essa letra.")
            continue

        if tentativa in palavra:
            letras_certas.add(tentativa)
            print("✅ Boa! A letra está na palavra.")
        else:
            letras_erradas.add(tentativa)
            tentativas -= 1
            print("❌ Ops! A letra não está na palavra.")

        if set(palavra) == letras_certas:
            print("\n🎉 Parabéns! Você venceu! A palavra era:", palavra)
            break
    else:
        print("\n💀 Você perdeu! A palavra era:", palavra)

# Iniciar o jogo
forca()