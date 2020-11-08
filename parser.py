# parser.py
import requests
from bs4 import BeautifulSoup
import json
import os

# HTTP GET Request
req = requests.get('https://beomi.github.io/beomi.github.io_old/')

# HTML 소스 가져오기
html = req.text

# requests 라이브러리를 이용한 크롤링 예제
# HTTP Header 가져오기
header = req.headers
# HTTP Status 가져오기 (200: 정상)
status = req.status_code
# HTTP가 정상적으로 되었는지 (True/False)
is_ok = req.ok

# bs4 이용하기
# 처음 인자는 html 소스 코드, 두 번째 인자는 어떤 parser 를 이용할지 명시
# html.parser 는 Python 내장 메서드
soup = BeautifulSoup(html, 'html.parser')
print(soup)

# 모든 제목 추출하기
my_soup = soup.select(
    'body > h3 > a'
)
print(my_soup)

for title in my_soup:
    # 태그 안의 텍스트 추출
    print(title.text)
    # 태그 속성 가져오기 (ex: href)
    print(title.get('href'))

# 크롤링 데이터를 json 형태로 저장하기
BASE_DIR = os.path.dirname(os.path.abspath(__file__)) # 현재 파일 디렉토리

data = {} # empty dictionary

for title in my_soup:
    data[title.text] = title.get('href')

with open(os.path.join(BASE_DIR, 'result.json'), 'w+') as json_file:
    json.dump(data, json_file)