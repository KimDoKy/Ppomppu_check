from django.urls import path
from .views import run_crawling

urlpatterns = [
    path('crawling/', run_crawling)
    ]
