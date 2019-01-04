from selenium import webdriver
import time

# headless 모드로 실행해보려고 했으나 find_elements 에서 에러나서 포기
# options = webdriver.ChromeOptions()
# options.add_argument('headless')
# options.add_argument('window-size=1920x1080')
# options.add_argument("disable-gpu")
# options.add_argument("user-agent=Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36")
# options.add_argument("proxy-server=localhost:8080")
# options.add_argument("lang=ko_KR")
# driver = webdriver.Chrome('D:/DownLoad/chromedriver_win32/chromedriver.exe', chrome_options=options)
#
# user_agent = driver.find_element_by_css_selector('#user-agent').text
# plugins_length = driver.find_element_by_css_selector('#plugins-length').text
# languages = driver.find_element_by_css_selector('#languages').text
# webgl_vendor = driver.find_element_by_css_selector('#webgl-vendor').text
# webgl_renderer = driver.find_element_by_css_selector('#webgl-renderer').text
#
# print('User-Agent: ', user_agent)
# print('Plugin length: ', plugins_length)
# print('languages: ', languages)
# print('WebGL Vendor: ', webgl_vendor)
# print('WebGL Renderer: ', webgl_renderer)

# ########### 네이버 로그인 테스트
# # driver = webdriver.Chrome('D:/DownLoad/chromedriver_win32/chromedriver.exe')
# driver.get('https://nid.naver.com/nidlogin.login')
#
# driver.execute_script("Object.defineProperty(navigator, 'plugins', {get: function() {return[1, 2, 3, 4, 5];},});")
# driver.execute_script("Object.defineProperty(navigator, 'languages', {get: function() {return ['ko-KR', 'ko']}})")
# driver.execute_script("const getParameter = WebGLRenderingContext.getParameter;WebGLRenderingContext.prototype.getParameter = function(parameter) {if (parameter === 37445) {return 'NVIDIA Corporation'} if (parameter === 37446) {return 'NVIDIA GeForce GTX 980 Ti OpenGL Engine';}return getParameter(parameter);};")
# driver.implicitly_wait(3)
# driver.get_screenshot_as_file('naver_main.png')
#
# # user_agent = driver.find_element_by_css_selector('#user-agent').text
#
# ## <selenium.webdriver.chrome.webdriver.WebDriver (session="bbf10f54a4a4050e6517516755326766")>
# # print(driver.find_element_by_name('id'))
# # driver.find_element_by_name('id').send_keys('talesof81')
# # driver.find_element_by_name('pw').send_keys('40611406az')
# # # 로그인 버튼을 눌러주자.
# # driver.find_element_by_xpath('//*[@id="frmNIDLogin"]/fieldset/input').click()
# exit(0)

# 오 이거 좋은거 같은데??

########

####################### yes 24 로그인
driver = webdriver.Chrome('D:/DownLoad/chromedriver_win32/chromedriver.exe')
driver.implicitly_wait(3)
driver.get('https://www.yes24.com/Templates/FTLogin.aspx')

# driver.maximize_window()

print("너님 아이디를 입력 : ")
str = input()
print("너님 비번을 입력 : ")
strPass = input()

# driver.find_element_by_class_name('btnlogin').click()
driver.find_element_by_id('SMemberID').send_keys(str)
driver.find_element_by_id('SMemberPassword').send_keys(strPass)
driver.find_element_by_id('btnLogin').click()
# 이제부터 yes24를 크롤링 해볼 수 있겠다.
# 베스트셀러 목록 csv 나 json 으로 빼는 일을 해볼 수 있을거 같고.
######################################### yes 24

time.sleep(5)
driver.close()

