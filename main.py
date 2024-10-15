import yt_dlp
import os

# Solicita a URL do vídeo
video_url = input("Digite a URL do vídeo do YouTube: ")

# Obtém o diretório de downloads do usuário
downloads_dir = os.path.join(os.path.expanduser("."), "downloads")

# Define opções para o download
ydl_opts = {
    'format': 'bestaudio/best',
    'outtmpl': os.path.join(downloads_dir, '%(title)s.%(ext)s'),
    'postprocessors': [{
        'key': 'FFmpegExtractAudio',
        'preferredcodec': 'mp3',
        'preferredquality': '192',
    }],
}

try:
    # Baixa o áudio do vídeo usando o yt-dlp
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([video_url])

    print("Áudio baixado com sucesso na pasta Downloads!")
except Exception as e:
    print(f"Ocorreu um erro: {e}")
