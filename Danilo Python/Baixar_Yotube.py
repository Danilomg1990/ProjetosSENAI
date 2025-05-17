from pytubefix import YouTube
#Url do video do  yotube
url="https://www.youtube.com/watch?v=jQMbuK6URws&list=PLHz_AreHm4dm24MhlWJYiR_Rm7TFtvs6S"

#Cria o objeto Youtube
yt=YouTube(url)

#Seleciona o string com melhor resolção
stream=yt.streams.get_highest_resolution()

#Baixa o video para o diretorio atual
stream.download("C:/Users/Aluno/Desktop/Danilo Python")
print("Download completo!")
