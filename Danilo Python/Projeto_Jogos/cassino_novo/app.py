from flask import Flask, render_template, request, session, redirect, url_for
import random

app = Flask(__name__)
app.secret_key = 'chave-secreta-para-session'

# Símbolos do caça-níquel (emojis)
simbolos = [
    '🍒', '🔔', '🍋', '💎', '7️⃣', '🍇', '🍉', '🍀', '👑', '💰',
    '🪙', '🎲', '⭐', '🃏', '🎁', '🔥', '🪄', '🧨', '🦄', '🌈',
    '🎩', '🛸', '👻', '🌟', '🪅', '🥇', '🔷', '💲', '🦜', '🍭',
    '🎈', '🌙', '☠️', '🐉', '🧿'
]

@app.route('/', methods=['GET', 'POST'])
def index():
    if 'saldo' not in session:
        session['saldo'] = 1000  # saldo inicial

    resultado = []
    mensagem = ""
    aposta = 10

    if request.method == 'POST':
        try:
            aposta = int(request.form['aposta'])
            if aposta <= 0:
                mensagem = "⚠️ Aposta inválida. Digite um valor positivo."
            elif aposta > session['saldo']:
                mensagem = "💸 Saldo insuficiente para esta aposta."
            else:
                # Realiza a rodada
                resultado = [random.choice(simbolos) for _ in range(3)]

                # Atualiza o saldo com base no resultado
                if resultado[0] == resultado[1] == resultado[2]:
                    ganho = aposta * 10
                    session['saldo'] += ganho
                    mensagem = f"💰 JACKPOT! Você ganhou {ganho} moedas!"
                elif resultado[0] == resultado[1] or resultado[1] == resultado[2] or resultado[0] == resultado[2]:
                    ganho = aposta * 2
                    session['saldo'] += ganho
                    mensagem = f"✨ Dois símbolos iguais! Você ganhou {ganho} moedas!"
                else:
                    session['saldo'] -= aposta
                    mensagem = "😢 Tente novamente!"
        except ValueError:
            mensagem = "⚠️ Insira um valor numérico válido para a aposta."

    return render_template('index.html', resultado=resultado, mensagem=mensagem, saldo=session['saldo'])

@app.route('/resetar')
def resetar():
    session.pop('saldo', None)
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
