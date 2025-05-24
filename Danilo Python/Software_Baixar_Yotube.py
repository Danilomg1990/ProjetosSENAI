import tkinter as tk
from tkinter import filedialog, messagebox
from pytubefix import YouTube

def selecionar_pasta():
    pasta = filedialog.askdirectory()
    if pasta:
        caminho_entry.delete(0, tk.END)
        caminho_entry.insert(0, pasta)

def baixar_video():
    url = url_entry.get()
    caminho = caminho_entry.get()

    if not url or not caminho:
        messagebox.showerror("Erro", "Por favor, insira a URL e selecione o caminho.")
        return

    try:
        yt = YouTube(url)
        stream = yt.streams.get_highest_resolution()
        stream.download(caminho)
        messagebox.showinfo("Sucesso", "Download completo!")
    except Exception as e:
        messagebox.showerror("Erro", f"Ocorreu um erro: {e}")

# Criar janela
janela = tk.Tk()
janela.title("Downloader de Vídeos do YouTube")
janela.geometry("500x200")

# URL
tk.Label(janela, text="URL do vídeo:").pack(pady=5)
url_entry = tk.Entry(janela, width=60)
url_entry.pack(pady=5)

# Caminho
tk.Label(janela, text="Caminho para salvar:").pack(pady=5)
caminho_frame = tk.Frame(janela)
caminho_entry = tk.Entry(caminho_frame, width=45)
caminho_entry.pack(side=tk.LEFT, padx=5)
selecionar_btn = tk.Button(caminho_frame, text="Selecionar Pasta", command=selecionar_pasta)
selecionar_btn.pack(side=tk.LEFT)
caminho_frame.pack(pady=5)

# Botão de download
download_btn = tk.Button(janela, text="Baixar Vídeo", command=baixar_video)
download_btn.pack(pady=10)

# Executar
janela.mainloop()