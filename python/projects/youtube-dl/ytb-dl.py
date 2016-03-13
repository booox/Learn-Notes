import youtube_dl

# url = 'https://www.youtube.com/watch?v=idexNu0SZpU'
# url = 'https://www.youtube.com/watch?v=Wi848QqLbdo'
# url = 'https://www.youtube.com/watch?v=fXsiW7A--dY'
# ul = 'https://www.youtube.com/watch?v=uuiusIIOqY4'
# url = 'https://www.youtube.com/watch?v=kMLWDbyjfq4'
# ul = 'https://www.youtube.com/watch?v=42CYiUtGafQ'
url = 'https://www.youtube.com/watch?v=hzTZaa4ORKw'


ydl_opts = {
    'format' : 'flv',
}
with youtube_dl.YoutubeDL(ydl_opts) as ydl:
    ydl.download([url,])
    
    
