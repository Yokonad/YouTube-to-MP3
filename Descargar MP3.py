import os
from yt_dlp import YoutubeDL
from colorama import Fore, Style, init

# Inicializa colorama
init(autoreset=True)

def descargar_musica_youtube(url):
    ruta_destino = "C:/Users/USUARIO/Desktop/MP3"
    
    if not os.path.exists(ruta_destino):
        print(f"{Fore.YELLOW}Creando la carpeta de destino: {ruta_destino}{Style.RESET_ALL}")
        os.makedirs(ruta_destino)
    
    opciones = {
        'format': 'bestaudio/best',
        'outtmpl': os.path.join(ruta_destino, '%(title)s.%(ext)s'),
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',
        }],
        'progress_hooks': [progreso_descarga],
    }

    try:
        print(f"{Fore.GREEN}Iniciando la descarga y conversión...{Style.RESET_ALL}")
        with YoutubeDL(opciones) as ydl:
            ydl.download([url])
            print(f"{Fore.GREEN}Descarga y conversión completadas con éxito.{Style.RESET_ALL}")
    except Exception as e:
        print(f"{Fore.RED}Error al descargar o convertir el video: {e}{Style.RESET_ALL}")

def progreso_descarga(d):
    if d['status'] == 'downloading':
        porcentaje = d['_percent_str']
        velocidad = d['_speed_str']
        print(f"{Fore.CYAN}Descargando... {porcentaje} a {velocidad}{Style.RESET_ALL}", end="\r")
    elif d['status'] == 'finished':
        print(f"\n{Fore.GREEN}Descarga completada: {d['filename']}{Style.RESET_ALL}")

def es_lista_reproduccion(url):
    return 'playlist' in url

if __name__ == "__main__":
    url_video = input(f"{Fore.MAGENTA}Introduce la URL de YouTube: {Style.RESET_ALL}").strip()
    
    if url_video:
        print(f"{Fore.YELLOW}Iniciando descarga...{Style.RESET_ALL}")
        descargar_musica_youtube(url_video)
    else:
        print(f"{Fore.RED}Por favor, ingresa una URL válida.{Style.RESET_ALL}")
