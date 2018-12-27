from pytube import Youtube
yt = Youtube('https://www.youtube.com/watch?v=P4daXwKm3TU')
yt.streams.filter(progressive=True, file_extension='mp4').order_by('resolution').desc().first().download()

