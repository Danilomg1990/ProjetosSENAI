from moviepy.editor import VideoFileClip, AudioFileClip
import whisper
from gtts import gTTS
from deep_translator import GoogleTranslator
import os

# Caminho do vídeo original
input_video = "video_ingles.mp4"
output_audio_pt = "audio_pt.mp3"
output_video_final = "video_dublado.mp4"

# 1. Extrair áudio do vídeo
video = VideoFileClip(input_video)
video.audio.write_audiofile("temp_audio.wav")

# 2. Transcrever áudio com Whisper
model = whisper.load_model("base")  # você pode usar "small", "medium", "large"
result = model.transcribe("temp_audio.wav", language="en")

# 3. Traduzir texto para português
texto_em_ingles = result["text"]
texto_em_portugues = GoogleTranslator(source='en', target='pt').translate(texto_em_ingles)

# 4. Gerar áudio em português com gTTS
tts = gTTS(texto_em_portugues, lang='pt')
tts.save(output_audio_pt)

# 5. Substituir áudio original pelo dublado
audio_pt = AudioFileClip(output_audio_pt)
video = video.set_audio(audio_pt)
video.write_videofile(output_video_final)

# 6. Limpeza
os.remove("temp_audio.wav")
os.remove(output_audio_pt)

print("✅ Dublagem concluída. Vídeo salvo como:", output_video_final)