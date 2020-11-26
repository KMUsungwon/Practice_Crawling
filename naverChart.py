from bs4 import BeautifulSoup
import requests
#네이버 실시간 급상승 검색어 크롤링

# User-Agent 설정
headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.122 Safari/537.36'}
# 네이버 데이터랩 주소
url = 'https://datalab.naver.com/keyword/realtimeList.naver?where=main'

# url 주소를 읽고 bs 형태로 변환
res = requests.get(url, headers=headers)
soup = BeautifulSoup(res.text, 'html.parser')

my_chart = soup.select('span.item_title')
num = 1
for chart in my_chart:
    print('%d'%num+'. '+chart.get_text())
    num = num+1