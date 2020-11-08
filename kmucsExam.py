import requests
from bs4 import BeautifulSoup

req = requests.get('https://cs.kookmin.ac.kr/') #국민대학교 소프트웨어융합대학 주소 가져오기
html = req.text # html 코드 저장

soup = BeautifulSoup(html, 'html.parser') # BS 형태의 html 코드 저장

# 공지사항 항목 추출
my_title = soup.select(
    '#tab-item0 > ul > li > a'
)
# print(my_title)

data = {} # empty dictionary

# 공지사항 제목과 주소를 key : value 형태로 저장
for title in my_title:
    data[title.text] = title.get('href')

print(data.keys())
print(data.values())