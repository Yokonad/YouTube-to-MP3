
# Guía Completa: Configuración de FFmpeg y Descarga de MP3 desde YouTube con Python

## Introducción
En esta guía, aprenderás a configurar FFmpeg en tu sistema, instalar las librerías necesarias y escribir un script en Python para descargar música de YouTube o YouTube Music en formato MP3. Además, abordaremos los errores más comunes y sus soluciones.

---

## Requisitos Previos
- Sistema operativo Windows.
- Python instalado en tu sistema.
- Conexión a internet estable.

---

## Paso 1: Descarga e Instalación de FFmpeg

1. **Descarga FFmpeg:**
   - Visita [FFmpeg Download](https://ffmpeg.org/download.html).
   - Selecciona "Windows Builds" y haz clic en un enlace confiable como [Gyan.dev FFmpeg Builds](https://www.gyan.dev/ffmpeg/builds/).
   - Descarga el archivo `ffmpeg-release-essentials.zip`.

2. **Extrae FFmpeg:**
   - Extrae el archivo ZIP en una ubicación como `C:\ffmpeg`.
   - La estructura de carpetas debe ser:
     ```
     C:\ffmpeg\
         ├── bin\
         ├── doc\
         ├── include\
         ├── lib\
     ```

3. **Agrega FFmpeg al PATH de Windows:**
   - Abre "Editar las variables de entorno del sistema".
   - En la sección "Variables del sistema", selecciona `Path` y haz clic en Editar.
   - Agrega la ruta `C:\ffmpeg\bin`.
   - Guarda los cambios y verifica en la terminal con:
     ```
     ffmpeg -version
     ```

---

## Paso 2: Instalación de Librerías Python
En la terminal de tu sistema o en Visual Studio Code (VSC), instala las siguientes librerías:
```bash
pip install pytube pydub yt-dlp
```

---

## Paso 3: Código en Python para Descargar MP3
Guarda el siguiente código en un archivo llamado `descargar_mp3.py`:

```python
import os
from yt_dlp import YoutubeDL

def descargar_musica_youtube(url):
    ruta_destino = "C:/Users/USUARIO/Desktop/MP3"
    
    if not os.path.exists(ruta_destino):
        print(f"Creando la carpeta de destino: {ruta_destino}")
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
        print("Iniciando la descarga y conversión...")
        with YoutubeDL(opciones) as ydl:
            ydl.download([url])
            print("Descarga y conversión completadas con éxito.")
    except Exception as e:
        print(f"Error al descargar o convertir el video: {e}")

def progreso_descarga(d):
    if d['status'] == 'downloading':
        porcentaje = d['_percent_str']
        velocidad = d['_speed_str']
        print(f"Descargando... {porcentaje} a {velocidad}", end="\r")
    elif d['status'] == 'finished':
        print(f"\nDescarga completada: {d['filename']}")

if __name__ == "__main__":
    url_video = input("Introduce la URL del video de YouTube: ").strip()
    if url_video:
        descargar_musica_youtube(url_video)
    else:
        print("Por favor, ingresa una URL válida.")
```

---

## Errores Comunes y Soluciones

### Error: HTTP Error 403: Forbidden
**Causa:**
- Restricciones en la URL proporcionada.
- Cambios en la API de YouTube que afectan a `pytube`.

**Soluciones:**
1. Actualiza la biblioteca `pytube`:
   ```bash
   pip install --upgrade pytube
   ```
2. Verifica la URL: Asegúrate de que la URL es válida y corresponde a un video que puedes reproducir en el navegador.
3. Usa autenticación OAuth:
   Cambia esta línea:
   ```python
   yt = YouTube(url)
   ```
   Por:
   ```python
   yt = YouTube(url, use_oauth=True, allow_oauth_cache=True)
   ```
4. Cambia de URL: Si el problema persiste, prueba con otro video.
5. Usa `yt-dlp` como alternativa: El código proporcionado utiliza `yt-dlp`, una herramienta más robusta para descargas desde YouTube.

### Error: FileNotFoundError: [WinError 2]
**Causa:**
- FFmpeg no está configurado correctamente en el PATH.

**Solución:**
- Verifica que `C:\ffmpeg\bin` esté agregado al PATH del sistema.
- Confirma que el comando `ffmpeg -version` funciona en la terminal.

---

## Resumen de Comprobaciones

Antes de ejecutar el programa:
1. Verifica que FFmpeg está configurado correctamente:
   ```bash
   ffmpeg -version
   ```
2. Asegúrate de que las librerías están instaladas:
   ```bash
   pip show pytube
   pip show pydub
   pip show yt-dlp
   ```
3. Ejecuta el script en Visual Studio Code o cualquier terminal:
   ```bash
   python descargar_mp3.py
   ```
