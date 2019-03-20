from celery import task
from django.conf import settings
from keywords.models import Keywords
from .utils.crawling import craw_item
from .utils.save_db import save_db
from .utils.diff_data import diff_data
from .utils.matching import matching_keyword

host = settings.CONF_FILES['AWS']['cache']

@task
def crawling():
    global host
    # 뽐뽐 게시판을 크롤링
    url = 'http://www.ppomppu.co.kr/zboard/zboard.php?id=ppomppu&page=1'
    contents = craw_item(url)
    # 크롤링한 데이터를 DB에 저장
    save_db(contents)
    # 바로 이전에 크롤링한 캐시와 비교하여
    # 업데이트 된 데이터만 추출
    new_datas = diff_data(contents, host)
    # 키워드 리스트를 불러와서 업데이트된 데이터와 비교하고
    # 매칭 조건이 일치하면 해당 유저에게 안내 메일을 발송
    # 각 키워드별로 유저가 다르기 때문에
    # 키워드를 비교하여 일치하면 send_mail 함수를 동작시킨다.
    keywords = Keywords.objects.filter(alarm=True)
    for key in new_datas:
        matching_keyword(keywords, new_datas[key])
    # 크롤링한 데이터를 redis 캐시로 저장함
    return contents
