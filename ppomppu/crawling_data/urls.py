from django.urls import path
from .views import run_crawling, CrawlingListView

urlpatterns = [
    path('crawling/', run_crawling),
    path('', CrawlingListView.as_view()), 
    ]
