from bs4 import BeautifulSoup
import requests

# 네이버 블로그 검색결과 가져오기

# 검색어 입력 받은 후 크롤링 할 페이지 저장
def getPage(keyword):
    url = 'https://search.naver.com/search.naver?query=%s&nso=&where=blog&sm=tab_viw.all'%keyword
    data = requests.get(url)


    return data.text # 페이지 정보를 리턴

# soup 를 통해 가져올 정보 추출 후 출력
def info(pageInfo):
    soup = BeautifulSoup(pageInfo, 'html.parser')
    my_soup = soup.find_all(class_='total_tit')

    # 왜 30개 밖에 출력이 안되는지?
    for title in my_soup:
        print(title.text)
        print(title.attrs['href'])

key = input("input keyword : ")
page_info = getPage(key)
info_content = info(page_info)