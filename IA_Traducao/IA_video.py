import whisper
from deep_translator import GoogleTranslator

# 1. Carregar modelo Whisper
model = whisper.load_model("medium")  # pode usar "small", "medium", "large" para mais precisão

# 2. Transcrever o áudio do vídeo
result = model.transcribe("1-Introdução.mp4")  # insira o caminho do seu vídeo
texto_em_ingles = result["1-Introdução(Texto).txt"]

# 3. Traduzir para português
traducao = GoogleTranslator(source='en', target='pt').translate(texto_em_ingles)

# 4. Salvar em arquivo
with open("legenda_traduzida.txt", "w", encoding="utf-8") as f:
    f.write(traducao)

print("Tradução concluída! Legenda salva em 'legenda_traduzida.txt'")