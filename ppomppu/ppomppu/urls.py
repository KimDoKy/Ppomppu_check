from django.contrib import admin
from django.urls import path, include
from users.views import KakaoLogin, redirect_view
from .yasg import *


urlpatterns = [
    path('admin/', admin.site.urls),
    path('run/', include('crawling_data.urls')),
    path('users/', include('users.urls')),
    path('keywords/', include('keywords.urls')),
    path('boards/', include('boards.urls')),
    path('rest-auth/', include('rest_auth.urls')),
    path('rest-auth/registration/', include('rest_auth.registration.urls')),
    path('rest-auth/registration/<key>/', redirect_view, name='account_confirm_email'),
    path('rest-auth/kakao/', KakaoLogin.as_view(), name='socialaccount_signup'),

    # api document generation with drf_yasg
    path('v1/redoc/', schema_view_v1.with_ui('redoc', cache_timeout=0), name='schema-redoc-v1'),
]
