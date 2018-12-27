from selenium import webdriver

## path = "드라이버 파일 위치"  # ex. C:/downloads/chromedriver.exe

path = "D:\DownLoad\chromedriver_win32\chromedriver.exe"

# 조금만 기다리면 selenium으로 제어할 수 있는 브라우저 새창이 뜬다
driver = webdriver.Chrome(path)
