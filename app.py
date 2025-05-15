# app.py
from flask import Flask, render_template, request
import os
from yt_dlp import YoutubeDL

app = Flask(__name__)

def baixar(url, tipo):
    if tipo == 'video':
        pasta = 'video'
        formato = 'best[ext=mp4][acodec!=none]'
        ext = 'mp4'
    else:
        pasta = 'audio'
        formato = 'bestaudio[ext=m4a]/bestaudio'
        ext = 'mp3'

    os.makedirs(pasta, exist_ok=True)

    ydl_opts = {
        'format': formato,
        'outtmpl': os.path.join(pasta, '%(title)s.%(ext)s'),
        'quiet': True,
        'no_warnings': True,
    }

    if tipo == 'audio' and ext == 'mp3':
        ydl_opts['postprocessors'] = [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',
        }]

    with YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])

@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        url = request.form.get('url')
        tipo = request.form.get('tipo')
        try:
            baixar(url, tipo)
            return render_template('index.html', mensagem='Download concluído!', url='', tipo='')
        except Exception as e:
            return render_template('index.html', mensagem=f'Erro: {e}', url=url, tipo=tipo)
    return render_template('index.html', url='', tipo='')

@app.route('/downloads')
def downloads():
    video_dir = 'video'
    audio_dir = 'audio'

    videos = os.listdir(video_dir) if os.path.exists(video_dir) else []
    audios = os.listdir(audio_dir) if os.path.exists(audio_dir) else []

    return render_template('downloads.html', videos=videos, audios=audios)

if __name__ == '__main__':
    app.run(debug=True)
