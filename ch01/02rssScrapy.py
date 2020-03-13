# -*- coding:utf-8 -*-

# RSS를 어떻게하지
# Feedparser_rss를 파싱할때 사용한데요

# URL = http://www.aladin.co.kr/rss/special_new/351

import feedparser

rss=feedparser.parse("http://www.aladin.co.kr/rss/special_new/351")  # parse는 FeedParserDict 클래스의 객체를 반환함 / 피드 정보는 feed 키에 들어 있음
print(rss["feed"]["title"]) # 분야별 신간 특선 - 컴퓨터/모바일 / 피드정보는 Feed 키에 들어 있음

print(rss["entries"]) # RSS의 엔트리(item 요소)는 다음과 같음

for content in rss["entries"]:
    print(content["title"])
    print(content["link"]) # title, link 출력

print(rss.version) # rss20 / rss 버전확인함


