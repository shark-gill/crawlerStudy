# -*- coding:utf-8 -*-

# 라이브러리 설치하기
# Requests_간단하게 웹 페이지를 추출할 수 있게 해주는 라이브러리
# lxml_C 언어로 작성된 libxml2, libxslt의 파이썬 바인딩 / 유연하게 xml, html 조작할 수 있는 라이브러리
# cssselect_css 선택자 라이브러리

import requests

r=requests.get("https://datalab.naver.com/")
print(r.status_code) # 200
print(r.text) # body 추출 / html 로나옴

# Xpath 와 css 선택자
# XPath(XML Path Language)
# cssselect_.class / # id

# URL : https://wikibook.co.kr/python-crawler/
# XPath_//*[@id="content"]/div[1]/div[2]/h1
# selector_#content > div:nth-child(1) > div.col-md-9 > h1

import lxml.html

# HTML 소스 코드를 읽어 들임
r=requests.get("https://wikibook.co.kr/python-crawler/") # URL elements 요청
print(r.status_code) # r 상태 확인
html=r.text # r의 html을 출력

# HTML을 HtmlElement 객체로 변환
root=lxml.html.fromstring(html) # htmlelement 클래스의 객체로 변환

# XPath로 요소를 추출함
titleElement=root.xpath('//*[@id="content"]/div[1]/div[2]/h1')
print(titleElement[0].text) # title 나옴 / 여기서 [0]은 Xpath지정 요소가 여러개일수 도 있어서 리스트로 반환함
print(titleElement[0].tag) # h1
print(titleElement[0].attrib) # {'class': 'main-title'}

# CSS 선택자
# #book-stores > li:nth-child(1) > a > img
# #book-stores > li:nth-child(2) > a > img
# #book-stores > li:nth-child(3) > a > img
# #book-stores > li:nth-child(4) > a > img

import requests
import lxml.html

r=requests.get("https://wikibook.co.kr/python-crawler/")
html=r.text
root=lxml.html.fromstring(html) # htmlelement 클래스의 객체로 변환 / 매개변수로 지정 fromstring 머야

# CSS 선택자를 사용하여 요소를 추출함
linkAs=root.cssselect('#book-stores>li>a')

# for 반복문으로 추출한 요소의 href의 속성을 추출함
for linkA in linkAs:
    print(linkA.attrib["href"])

