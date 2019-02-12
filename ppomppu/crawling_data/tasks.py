from celery import task
from .utils.crawling import craw_item
from .utils.save_db import save_db

@task
def crawling():
    url = 'http://www.ppomppu.co.kr/zboard/zboard.php?id=ppomppu&page=1'
    print(url)
    contents = craw_item(url)
    print(contents)
    save_db(contents)
    print('-------------123-------------')

