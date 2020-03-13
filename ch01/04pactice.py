# -*- coding:utf-8 -*-

## with 구문으로 close 메서드 누수 막기

import json
import time

import requests

PAGE_URL_LIST=[
    'http://example.com/1.page',
    'http://example.com/2.page',
    'https://dgkim5360.tistory.com/entry/not-JSON-serializable-error-on-python-json'
]

def fetch_pages():
    """페이지의 내용을 추출합니다"""
    # 처리 기록 전용 로그 파일과 오류 기록 전용 로그 파일을 append 모드로 엽니다
    with open('crawler_info.log', 'a') as f_info_log, \
        open('crawler_error.log', 'a') as f_error_log:

        # 추출 내용을 저장할 딕셔너리
        page_contents={}

        # 터미널에 처리 시작을 출력하고, 로그 파일에도 메시지를 출력함
        msg="[INFO] Starting Crawling"
        print(msg)
        f_info_log.write(msg)

        for page_url in PAGE_URL_LIST:
            try:
                r=requests.get(page_url, timeout=30)
                r.raise_for_status() # 응답에 문제가 생기면 예외를 발생함
            
            except requests.exceptions.RequestException as e:
                # requests와 관련된 예외가 발생하면,
                # 터미널과 오류 로그에 오류를 출력함
                msg="[ERROR] {exception}".format(exception=e)
                print(msg)
                f_error_log.write(msg)
                continue # 예외가 발생해도 반복을 중지하지말고 건너뛰라
        
        # 정상적으로 내용을 추출하였다면 딕셔너리에 내용을 저장함
        page_contents[page_url]=r.text
        time.sleep(1) # 상대 사이트에 대한 부하를 고려하여 살짝 줘봤다

    return page_contents

if __name__=='__main__':
    page_contents=fetch_pages()
    with open('page_contents.json', 'w') as f_page_contents:
        json.dump(page_contents, f_page_contents, ensure_ascii=False)