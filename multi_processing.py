import requests
from bs4 import BeautifulSoup as bs
import time

# 멀티 프로세싱을 위한 라이브러리
from multiprocessing import Pool

#블로그 게시글 링크 가져오기
def get_links():
    req = requests.get('https://beomi.github.io/beomi.github.io_old/')
    html = req.text
    soup = bs(html, 'html.parser')
    my_titles = soup.select(
        'body > h3 > a'
    )
    data = []

    for title in my_titles:
        data.append(title.get('href'))
    return data

def get_content(link):
    abs_link = 'https://beomi.github.io' + link
    req = requests.get(abs_link)
    html = req.text
    soup = bs(html, 'html.parser')

    print(soup.select('h1')[0].text) # h1 태그 확인하기

if __name__=='__main__':
    start_time = time.time()
    pool = Pool(processes=4) # 4개의 프로세스
    pool.map(get_content, get_links()) # get_content 함수를 호출, value는 get_links에서 리턴받은 값들
    # for link in get_links():
    #     get_content(link)
    print("---%s seconds ---" % (time.time() - start_time)) # 단일 프로세스 사용 시 약 19초
    # 멀티 프로세스 사용 시 약 3.8초