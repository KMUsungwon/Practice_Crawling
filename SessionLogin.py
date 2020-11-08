import requests
from bs4 import BeautifulSoup as bs
# 로그인할 유저 정보 입력
LOGIN_INFO = {
    'userId': 'myID',
    'userPassword': 'myPassWord'
}

# Session 생성
with requests.Session() as s:
    # POST url 및 전송할 데이터 지정
    login_req = s.post('https://www.clien.net/service/login', data=LOGIN_INFO)
    print(login_req.status_code) # result 404

    # _csrf 를 지정하여 세션 로그인 해보기
    first_page = s.get('https://www.clien.net/service')
    html = first_page.text
    soup = bs(html, 'html.parser')
    csrf = soup.find('input', {'name':'_csrf'}) # input 태그 중 name 값이 _csrf 인 것을 찾는다.
    print(csrf['value']) # 6d9c5952-a782-4805-9dd9-c6028de6dc9d 이런 코드 값 출력. 매 실행마다 바뀜

    # 위에서 정의한 LOGIN_INFO 에 _csrf 추가하기
    # {**dic1, **dic2} 는 두 개의 dictionary 를 합치는 방법
    # key = _csrf 로 하고 value 는 csrf 의 value 값을 넣어줌
    LOGIN_INFO = {**LOGIN_INFO, **{'_csrf':csrf['value']}}
    print(LOGIN_INFO)

    login_req = s.post('https://www.clien.net/service/login', data=LOGIN_INFO)
    print(login_req.status_code)

    # 세션 로그인 실패 시
    if login_req.status_code != 200:
        raise Exception('로그인에 실패했습니다.')

    # 세션 로그인 성공 시 공지사항 크롤링
    # 사이트 이용규칙 제목 가져오기

    post_one = s.get('https://www.clien.net/service/board/rule/10707403')
    html = post_one.text
    soup = bs(html, 'html.parser')
    title = soup.select('#div_content > div.post_title.symph_row > h3 > span')
    print(title)