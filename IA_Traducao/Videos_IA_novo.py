from moviepy.editor import VideoFileClip, AudioFileClip, concatenate_audioclips
import whisper
from gtts import gTTS
from deep_translator import GoogleTranslator
import os

# Caminho do vídeo original
input_video = os.path.join("IA_Traducao", "introducao.mp4")
output_audio_final = "audio_pt_final.mp3"
output_video_final = "video_dublado_sincronizado.mp4"

# Verifica se o vídeo existe
if not os.path.isfile(input_video):
    print(f"❌ Arquivo não encontrado: {input_video}")
    exit(1)

# 1. Extrair áudio do vídeo
video = VideoFileClip(input_video)
video.audio.write_audiofile("temp_audio.wav")

# 2. Carregar modelo Whisper
model = whisper.load_model("base")  # pode usar outros tamanhos

# 3. Transcrever com timestamps (segmentos)
result = model.transcribe("temp_audio.wav", language="en")

segments = result["segments"]  # lista com segmentos contendo 'start', 'end' e 'text'

print(f"Segmentos detectados: {len(segments)}")

# 4. Traduzir e gerar áudio por segmento, carregando com moviepy para concatenar
audio_clips = []

for i, seg in enumerate(segments):
    texto_original = seg["text"].strip()
    print(f"Segmento {i+1}/{len(segments)}: {texto_original}")

    # Traduzir
    texto_pt = GoogleTranslator(source='en', target='pt').translate(texto_original)

    # Gerar áudio com gTTS para o segmento
    tts = gTTS(texto_pt, lang='pt')
    segment_audio_path = f"segment_{i}.mp3"
    tts.save(segment_audio_path)

    # Carregar áudio com moviepy
    audio_clip = AudioFileClip(segment_audio_path)
    audio_clips.append(audio_clip)

# 5. Concatenar todos os áudios traduzidos
final_audio = concatenate_audioclips(audio_clips)
final_audio.write_audiofile(output_audio_final)

# Fecha os clips de áudio temporários e remove os arquivos
for clip, seg in zip(audio_clips, segments):
    clip.close()
    os.remove(f"segment_{segments.index(seg)}.mp3")

# 6. Substituir áudio no vídeo original
audio_pt_clip = AudioFileClip(output_audio_final)
video = video.set_audio(audio_pt_clip)
video.write_videofile(output_video_final)

# 7. Limpeza
os.remove("temp_audio.wav")
os.remove(output_audio_final)

print("✅ Dublagem concluída. Vídeo salvo como:", output_video_final)