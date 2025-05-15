import yt_dlp

url = "https://www.youtube.com/watch?v=_hL1pguiHX0"

with yt_dlp.YoutubeDL({}) as ydl:
    ydl.download([url])

print("Download concluído!")
