from django.http import HttpResponse
from .utils.crawling import craw_item
from .utils.save_db import save_db

def run_crawling(request):
    url = 'http://www.ppomppu.co.kr/zboard/zboard.php?id=ppomppu&page=1'
    contents = craw_item(url)
    save_db(contents)
    return HttpResponse("complate")
