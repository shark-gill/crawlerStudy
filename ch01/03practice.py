# -*- coding:utf-8 -*-

## 요청에 걸린 시간 출력하기

import time
import requests

PAGE_URL_LIST=[
    'http://example.com/1.page',
    'https://dzzienki.tistory.com/10',
    'https://www.google.com/search?sxsrf=ALeKk01cuhABwiOGOR4eG0EjFdJFGO62jQ%3A1584082002660&ei=UixrXvz2J6OTr7wProygkAI&q=%EC%8B%A4%EC%A0%84+%EC%98%81%EC%96%B4%EB%A1%9C&oq=%EC%8B%A4%EC%A0%84+%EC%98%81%EC%96%B4%EB%A1%9C&gs_l=psy-ab.3..0j0i30l4j0i5i30j0i8i30l4.6090.7050..7118...1.2..1.131.762.0j7......0....1..gws-wiz.......0i71j35i39j0i67j0i20i263.ZyLLI3M4pJ0&ved=0ahUKEwj858Co7ZboAhWjyYsBHS4GCCIQ4dUDCAs&uact=5'
]

  
        #     "페이지 URL:"+page_url+ ","+\
        #     "HTTP 상태 :"+str(res.status_code)+","+\
        #     "처리시간(초):"+str(res.elapsed.total_seconds())
        
        # 위의 구조는 str 자료형으로 변환하는 것을 잊어버려 오류발생할 수 있음

        # 아래와 같이 쓰면 자료형을 문자열로 출력할 때 좋데

for page_url in PAGE_URL_LIST:
    res=requests.get(page_url, timeout=30)
    print(
        "페이지 URL : {}, HTTP 상태 : {}, 처리시간(초) : {}".format(
            page_url,
            res.status_code,
            res.elapsed.total_seconds()
        )
    )

time.sleep(1) # 넌 필요하구나


## 로그 출력과 관련된 다양한 개선이 필요한 이유

import json
import time
import requests

def fetch_pages():
    """페이지의 내용을 추출합니다"""
    # 처리 기록 전용 로그 파일을 append 모드로 열자
    f_info_log=open('crawler_info.log', 'a')

    # 오류 기록 전용 로그 파일을 append 모드로 열자
    f_error_log=open('crawler_info.log', 'a')

    # 추출 내용을 저장할 딕셔너리
    page_contents={}

    # 터미널에 처리 시작을 출력하고, 로그 파일에도 메세지를 출력함
    msg = "crawling Start\n"
    print(msg)
    f_info_log.write(msg)

    for page_url in PAGE_URL_LIST:
        r=requests.get(page_url, timeout=30)
        try:
            r.raise_for_status() # 응답에 문제가 있으면 예외를 발생함
        except requests.exceptions.RequestException as e:
            # requests 와 관련된 예외가 발생하면
            # 터미널과 오류 로그에 오류를 출력함
            msg="[ERROR] {exception}\n".format(exception=e)
            print(msg)
            f_error_log.write(msg)
            continue # 예외 발생시 반복울 중지하는게 아니라 건너뜀

        # 정상적으로 내용을 추출했다면 딕셔너리에 내용을 저장함
        page_contents[page_url] = r.text
        time.sleep(1) # 상대 사이트에 대한 부하를 고려하여 요청 간격을 설정

    f_info_log.close()
    f_error_log.close()

    return page_contents


if __name__=='__main__':
    page_contents=fetch_pages
    f_page_contents=open('page_contents.json', 'w')
    json.dump(page_contents, f_page_contents, ensure_ascii=False)
    f_page_contents.close()



