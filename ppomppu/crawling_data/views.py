from django.http import HttpResponse
from rest_framework import generics
from .utils.crawling import craw_item
from .utils.save_db import save_db
from .models import CrawlingData
from .serializers import CrawlingSerializer

def run_crawling(request):
    url = 'http://www.ppomppu.co.kr/zboard/zboard.php?id=ppomppu&page=1'
    contents = craw_item(url)
    save_db(contents)
    return HttpResponse("complate")

class CrawlingListView(generics.ListAPIView):
    queryset = CrawlingData.objects.all()
    serializer_class = CrawlingSerializer
