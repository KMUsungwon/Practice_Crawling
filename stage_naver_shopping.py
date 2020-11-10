# 네이버 쇼핑 스토어 목록 크롤링 연습
import requests
from bs4 import BeautifulSoup

def crawl(keyword):
    url = "https://search.shopping.naver.com/search/all?query=%s&cat_id=&frm=NVSHATC"%keyword
    data = requests.get(url)
    return data.content # or data.text

def parse(pageString):
    bsObj = BeautifulSoup(pageString, 'html.parser')
    # my_soup = bsObj.select(
    #    '#__next > div > div.style_container__1YjHN > div > div.style_content_wrap__1PzEo > div.style_content__2T20F > ul > div > div > li > div > div.basicList_info_area__17Xyo > div.basicList_title__3P9Q7 > a'
    # )

    # Copy Selector 를 이용하는 것보다 훨씬 코드가 간결해진다.
    my_soup = bsObj.find_all(class_='basicList_link__1MaTN')
    data = []
    for title in my_soup:
        data.append(title.text)

    for i in range(0,len(data)):
        print(data[i])
    return "Finish"

key = input("Input Keyword : ")
pageString = crawl(key)
product = parse(pageString)
print(product)