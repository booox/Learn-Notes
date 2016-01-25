import youtube_dl

url = 'https://www.youtube.com/watch?v=idexNu0SZpU'
ydl_opts = {}
with youtube_dl.YoutubeDL(ydl_opts) as ydl:
    ydl.download([url,])