from django.urls import path
from .views import UserInfo, kakao_oauth

urlpatterns = [
    path('info/', UserInfo.as_view()),
    path('oauth/', kakao_oauth)
]
