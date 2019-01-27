from django.urls import path, include
from .views import KeywordListView

urlpatterns = [
    path('', KeywordListView.as_view()),
    ]
