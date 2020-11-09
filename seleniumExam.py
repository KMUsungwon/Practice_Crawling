# Selenium 프레임 워크를 이용한 네이버 로그인 제어 및 크롤링
from selenium import webdriver
from bs4 import BeautifulSoup
import time

driver = webdriver.Chrome('/Users/seongwon/Downloads/chromedriver')
driver.implicitly_wait(3)

driver.get('https://nid.naver.com/nidlogin.login') # 네이버 로그인 url 접근하기

# 네이버 로그인 창의 아이디 칸의 id=id, 로그인 칸의 id=pw

driver.find_element_by_id('id').send_keys('userId')
driver.find_element_by_id('pw').send_keys('userPw')

# 아이디 비밀번호 입력 후 로그인 버튼까지 클릭
driver.find_element_by_xpath('//*[@id="frmNIDLogin"]/fieldset/input').click()

time.sleep(20) # 네이버 로그인 보안 방지 이유로 시간 딜레이를 줌

# 네이버 페이 주문내역 크롤링 하기
driver.get('https://order.pay.naver.com/home')
html = driver.page_source
soup = BeautifulSoup(html, 'html.parser')
notices = soup.select('div.goods_item > div.goods_info > a > p')

for n in notices:
    print(n.text.strip())