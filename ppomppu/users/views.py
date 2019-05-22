from .models import CustomUser
from .serializers import UserSerializer
from allauth.socialaccount.providers.kakao.views import KakaoOAuth2Adapter
from rest_auth.registration.views import SocialLoginView
from rest_framework import generics

from django.http.response import HttpResponseRedirect

class UserInfo(generics.RetrieveAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = UserSerializer

    def get_object(self):
        return self.request.user


class KakaoLogin(SocialLoginView):
    adapter_class = KakaoOAuth2Adapter

import requests 
from django.conf import settings

def set_kakao_params(auth_code):
    grant_type = "authorization_code"
    client_id = settings.CONF_FILES['kakao']['client_id']
    redirect_uri = "http://localhost:8000/users/res/"
    params = {
        'code':auth_code,
        'grant_type':grant_type,
        'client_id':client_id,
        'grant_type':grant_type
        }
    return params

def get_access_token(params):
    url = "https://kauth.kakao.com/oauth/token"
    response = requests.post(url, params=params)
    res_data = response.json()
    access_token = res_data['access_token']
    token_type = res_data['token_type']
    refresh_token = res_data['refresh_token']
    res_params = {
        'access_token': access_token,
        'refresh_token':refresh_token
    }
    return res_params

from rest_framework.authtoken.models import Token

def save_user_token(auth_key, access_params):
    user = Token.objects.get(key=auth_key['key'])
    user_ob = CustomUser.objects.get(id=user.user_id)
    user_ob.refresh_token = access_params['refresh_token']
    user_ob.access_key = access_params['access_token']
    user_ob.save()

def get_auth_token(access_token):
    req_header = {'access_token':access_token}
    req_url = "http://localhost:8000/rest-auth/kakao/"
    response = requests.post(req_url, req_header)
    response_dict = response.json()
    return response_dict

def kakao_oauth(request):
    auth_code = request.GET["code"]
    req_params = set_kakao_params(auth_code)
    access_token_params = get_access_token(req_params)
    access_token = access_token_params['access_token']
    auth_key = get_auth_token(access_token)
    save_user_token(auth_key, access_token_params)
    print('meta----------------')
    # refer_url = request.META['HTTP_REFERER']
    refer_url = 'http://localhost:8080/'
    response = HttpResponseRedirect(refer_url, auth_key)
    response.set_cookie('token', auth_key['key'])
    return response