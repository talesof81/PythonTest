import urllib.request
import urllib.parse
import re
from pytube import YouTube
from pytube import Playlist

# where to save
SAVE_PATH = "D:/swingVideoUsingPython"  # to_do

# yt = YouTube("https://www.youtube.com/watch?v=1r_sr_jZdog&index=26&list=PLiq_gzpXMTH1n6tJgnCtwbwnjBv3jsG1D") #다운로드 받고자 하는 url을 입력합니다.
# #yt = YouTube("https://www.youtube.com/watch?v=RomrqnVfGxs") #다운로드 받고자 하는 url을 입력합니다.
# print(yt.title)
# yt.streams.first().download(SAVE_PATH)

#'https://www.youtube.com/watch?v=RomrqnVfGxs'
# 'https://www.youtube.com/watch?v=1GRENOP8wNE', \
# 'https://www.youtube.com/watch?v=g4ToYhtrw2c', \
# 'https://www.youtube.com/watch?v=gyMJZhYPOsQ', \

# 순수 색소폰 음악만 있다. 나중에 한번 써보자. 500개가 넘음.. ㄷㄷㄷ
# https://www.youtube.com/watch?v=PoLUuQgcCi4&list=PLqjMSN3S3_wOmCZIJCq7qF6lKCvXehbwq

# 여기도 200개 넘음 ㄷㄷ
# https://www.youtube.com/watch?v=YGKioh-EodA&list=PLiq_gzpXMTH1n6tJgnCtwbwnjBv3jsG1D

# pl = Playlist("https://www.youtube.com/watch?v=RomrqnVfGxs&list=PLG44HYCirdi6txE2SsYYPFCtuhYJ_Lz2z")
# pl = Playlist("https://www.youtube.com/watch?v=zVYG7jn-gX4&list=PLG44HYCirdi6PXsuSFasmq-8cOGL4z1rn")

pl = Playlist("https://www.youtube.com/watch?v=TWb4xTwR0I8&list=PL9mhQYIlKEhf0DKhE-E59fR-iu7Vfpife")

# pl.download_all(SAVE_PATH)
pl.populate_video_urls()

print(pl.playlist_url)
# print(pl.video_urls)

SAVE_PATH = SAVE_PATH + "_WebCrwaler"

# video_urls = "https://www.youtube.com/watch?v=qZMKY9d2D5k"

# 동영상 저장
# for i in pl.video_urls:
#
#     # filters out all the files with "mp4" extension
#     # d_video = regex_search(r'(?:v=|\/)([0-9A-Za-z_-]{11}).*', video_urls, group=1)
#     try:
#         yt = YouTube(i)
#         d_video = yt.streams.filter(progressive=True, file_extension='mp4').order_by('resolution').desc().first().download(SAVE_PATH)
#     except:
#         print("errorcase " + i )
#
# print('Task Completed!')

# try:
#     pl.download_all(SAVE_PATH)
# except :
#     print(pl.video_urls)

print('SAVE_PATH Task Completed!')

#query_string = urllib.parse.urlencode({"search_query" : input()})
#print(query_string)
#html_content = urllib.request.urlopen("http://www.youtube.com/results?" + query_string)
#html_content = "https://www.youtube.com/results?sp=CAI%253D&search_query=dax"
#search_results = re.findall(r'href=\"\/watch\?v=(.{11})', html_content.read().decode())

#html_content = urllib.request.urlopen("https://www.youtube.com/results?sp=CAI%253D&search_query=" + query_string)
#search_results = re.findall(r'href=\"\/watch\?v=(.{11})', html_content.read().decode())
#print(html_content)
#print(search_results)

### 같은 결과가 2개씩 나온다 이유가 뭘까??
query_string = 'daxhock'
html_content = urllib.request.urlopen("https://www.youtube.com/results?search_sort=video_date_uploaded&search_query=" + query_string)
search_results = re.findall(r'href=\"\/watch\?v=(.{11})', html_content.read().decode())
search_results = list(set(search_results))      ## 중복을 제거했다.
print(html_content)
print(search_results)

val = 0

for i in search_results:
    i = "http://www.youtube.com/watch?v=" + i
    print(i)
    val = val + 1

print(val)

exit(0)

## search_results = "https://www.youtube.com/watch?v=_YKYZ79uEXc"

for i in search_results:

    i = "http://www.youtube.com/watch?v=" + i
    print(i)

    yt = YouTube(i)

    # filters out all the files with "mp4" extension
    d_video = yt.streams.filter(progressive=True, file_extension='mp4').order_by('resolution').desc().first().download(SAVE_PATH)

    if val == 10:
        break
    else:
        print(val)

    val = val + 1

print('Task Completed!')


## 파일 찾는 다른 방법
# import urllib.request
# from bs4 import BeautifulSoup
#
# textToSearch = 'hello world'
# query = urllib.parse.quote(textToSearch)
# url = "https://www.youtube.com/results?search_query=" + query
# response = urllib.request.urlopen(url)
# html = response.read()
# soup = BeautifulSoup(html, 'html.parser')
# for vid in soup.findAll(attrs={'class':'yt-uix-tile-link'}):
#     print('https://www.youtube.com' + vid['href'])
#