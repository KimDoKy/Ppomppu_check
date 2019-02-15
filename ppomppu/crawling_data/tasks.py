from celery import task
# from multiprocessing import Process
from billiard import Process
import os
import re
from .models import CrawlingData
from keywords.models import Keywords
from .utils.crawling import craw_item
from .utils.save_db import save_db
from .utils.send_mail import send_mails


def matching_keyword(update_key, keywords):
    for key in keywords:
        if re.search(key.keyword, update_key.title):
            send_mails(key, update_key)

@task
def crawling():
    url = 'http://www.ppomppu.co.kr/zboard/zboard.php?id=ppomppu&page=1'
    contents = craw_item(url)
    save_db(contents)
    keywords = Keywords.objects.filter(alarm=True)
    # update_data는 redis를 통해 부하를 줄일 수 있을 것 같다.
    # 릭팩토링 예정
    update_data = CrawlingData.objects.filter(status=True)
    for update_key in update_data:
        matching_keyword(update_key, keywords)
