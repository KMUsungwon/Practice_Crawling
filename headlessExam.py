from selenium import webdriver

# driver = webdriver.Chrome('/Users/seongwon/Downloads/chromedriver')
#
# driver.get('http://naver.com')
# driver.implicitly_wait(3)
# driver.get_screenshot_as_file('naver_main.png') # 네이버 메인 페이지를 스크린 샷 후 저장
# driver.quit()

# Headless Chrome 사용하기

options = webdriver.ChromeOptions()
options.add_argument('headless') # headless 설정
options.add_argument('window-size=1920x1080') # 창의 크기
options.add_argument('disable-gpu') # GPU 사용하지 않음, 오류 시 --disable-gpu

driver = webdriver.Chrome('/Users/seongwon/Downloads/chromedriver', chrome_options=options)

driver.get('http://naver.com')
driver.implicitly_wait(3)
driver.get_screenshot_as_file('naver_main_headless.png')
driver.quit()