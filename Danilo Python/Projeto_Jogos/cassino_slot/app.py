from flask import Flask, render_template, request
import random

app = Flask(__name__)

# Símbolos do caça-níquel (emojis)
simbolos = [
    '🍒',  # Cereja
    '🔔',  # Sino
    '🍋',  # Limão
    '💎',  # Diamante
    '7️⃣', # Sete
    '🍇',  # Uva
    '🍉',  # Melancia
    '🍀',  # Trevo da sorte
    '👑',  # Coroa
    '💰',  # Saco de dinheiro
    '🪙',  # Moeda
    '🎲',  # Dado
    '⭐',  # Estrela
    '🃏',  # Curinga
    '🎁',  # Presente (bônus)
    '🔥',  # Fogo (símbolo especial)
    '🪄',  # Varinha mágica
    '🧨',  # Bombinha
    '🦄',  # Unicórnio
    '🌈',  # Arco-íris
    '🎩',  # Cartola
    '🛸',  # Disco voador
    '👻',  # Fantasma
    '🌟',  # Estrela brilhante
    '🪅',  # Piñata
    '🥇',  # Medalha de ouro
    '🔷',  # Diamante azul
    '💲',  # Cifrão
    '🦜',  # Papagaio
    '🍭',  # Pirulito
    '🎈',  # Balão
    '🌙',  # Lua
    '☠️',  # Caveira
    '🐉',  # Dragão
    '🧿',  # Olho grego
]

@app.route('/', methods=['GET', 'POST'])
def index():
    resultado = []
    mensagem = ""

    if request.method == 'POST':
        resultado = [random.choice(simbolos) for _ in range(3)]
        if resultado[0] == resultado[1] == resultado[2]:
            mensagem = "💰 JACKPOT! Você ganhou!"
        elif resultado[0] == resultado[1] or resultado[1] == resultado[2] or resultado[0] == resultado[2]:
            mensagem = "✨ Dois símbolos iguais!"
        else:
            mensagem = "😢 Tente novamente!"

    return render_template('index.html', resultado=resultado, mensagem=mensagem)

if __name__ == '__main__':
    app.run(debug=True)
