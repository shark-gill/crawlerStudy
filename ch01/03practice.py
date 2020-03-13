# -*- coding:utf-8 -*-

## 요청에 걸린 시간 출력하기

import time
import requests

PAGE_URL_LIST=[
    'https://www.google.com/webhp?hl=ko&sa=X&ved=0ahUKEwiCyuL07ZboAhVuHKYKHdGqDYsQPAgH',
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
    # 처리 기록 전용 로그 파일을 append 모드로 엽니다
    f_info_log=opne('03practice_info.log', 'a')
    
