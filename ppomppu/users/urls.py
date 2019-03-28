from django.urls import path
from .views import UserInfo

urlpatterns = [
    path('', UserInfo.as_view())
]