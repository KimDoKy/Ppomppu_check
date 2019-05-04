from .models import CustomUser
from .serializers import UserSerializer
from allauth.socialaccount.providers.kakao.views import KakaoOAuth2Adapter
from rest_auth.registration.views import SocialLoginView
from rest_framework import generics

from django.http.response import HttpResponse

class UserInfo(generics.RetrieveAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = UserSerializer

    def get_object(self):
        return self.request.user


class KakaoLogin(SocialLoginView):
    adapter_class = KakaoOAuth2Adapter

import requests 
from django.utils.six import BytesIO
from rest_framework.parsers import JSONParser

def kakao_oauth(request):
    url = "https://kauth.kakao.com/oauth/token"
    code = request.GET["code"]
    grant_type = "authorization_code"
    client_id = "9ed92fc9cf17c2073ca0554911152ad3"
    redirect_uri = "http://localhost:8000/users/res/"
    params = {
        'code':code,
        'grant_type':grant_type,
        'client_id':client_id,
        'grant_type':grant_type
        }
    response = requests.get(url, params=params)
    res_data = response.json()
    access_token = res_data['access_token']
    token_type = res_data['token_type']
    refresh_token = res_data['refresh_token']

    return HttpResponse(response, status=200)
