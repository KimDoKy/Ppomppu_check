from celery import task
# from multiprocessing import Process
from billiard import Process
import os
import re
import redis
import json
from .models import CrawlingData
from keywords.models import Keywords
from .utils.crawling import craw_item
from .utils.save_db import save_db
from .utils.send_mail import send_mails


conn = redis.StrictRedis(host='localhost', port=6379)

def matching_keyword(keywords, new_data):
    # 유저가 등록한 키워드와 업데이트된 타이틀을 비교한다.
    # 비교후 일치하면 안내메일을 발송한다.
    for key in keywords:
        if re.search(key.keyword, new_data['title']):
            send_mails(key, new_data)

def diff_data(contents):
    # redis에서 캐시를 불러와 업데이트 한 데이터와 비교한다.
    # in 함수로 중복여부를 판단하기 위해서
    # 캐시는 비교 값인 title로 구성된 list를 만든다.
    cache_title = []
    # 메일 발송에 필요한 정보는 dict가 필요함
    new_datas = {}
    # redis에서 마지막에 저장된 캐시를 불러옴
    # 캐시 데이터의 상태가 FAILURE인 경우 오류가 발생하기 때문에
    # celery 캐시 데이터의 갯수를 가지고와서
    # 최근순으로 읽어들인다.
    # 모두 오류이거나 없다면 cache_title은 빈 리스트를 반환한다.
    if conn.keys('celery*'):
        key_length = len(conn.keys('celery*'))
        for i in range(key_length - 1, 0, -1):
            before_cache = json.loads(conn.get(conn.keys('celery*')[i]))
            if before_cache['status'] == 'FAILURE':
                pass
            before_cache = before_cache['result']
            for key in before_cache:
                cache_title.append(before_cache[key]['title'])
    # 캐시 데이터와 업데이트 데이터를 비교한다.
    # return -> dict
    for key in contents:
        if contents[key]['title'] in cache_title:
            pass
        else:
            new_datas[key] = contents[key]
    return new_datas

@task
def crawling():
    # 뽐뽐 게시판을 크롤링
    url = 'http://www.ppomppu.co.kr/zboard/zboard.php?id=ppomppu&page=1'
    contents = craw_item(url)
    # 크롤링한 데이터를 DB에 저장
    save_db(contents)
    # 바로 이전에 크롤링한 캐시와 비교하여
    # 업데이트 된 데이터만 추출
    new_datas = diff_data(contents)
    # 키워드 리스트를 불러와서 업데이트된 데이터와 비교하고
    # 매칭 조건이 일치하면 해당 유저에게 안내 메일을 발송
    # 각 키워드별로 유저가 다르기 때문에
    # 키워드를 비교하여 일치하면 send_mail 함수를 동작시킨다.
    keywords = Keywords.objects.filter(alarm=True)
    for key in new_datas:
        matching_keyword(keywords, new_datas[key])
    # 크롤링한 데이터를 redis 캐시로 저장함
    return contents
