from django.urls import path
from .views import UserInfo, kakao_oauth, empty_view, change_username, membership_withdrawal

app_name = 'users'

urlpatterns = [
    path('info/', UserInfo.as_view()),
    path('oauth/', kakao_oauth),
    path('pass-reset/<uidb64>/<token>/', empty_view, name='password_reset_confirm'),
    path('change-username/', change_username),
    path('membership-withdrawal/', membership_withdrawal),
]
