from .models import CustomUser
from .serializers import UserSerializer
from django.conf import settings
from django.http.response import HttpResponseRedirect, HttpResponse
from django.shortcuts import redirect
from allauth.socialaccount.providers.kakao.views import KakaoOAuth2Adapter
from rest_auth.registration.views import SocialLoginView
from rest_framework import generics
from rest_framework.decorators import api_view
from rest_framework.authtoken.models import Token
from django.contrib.auth.hashers import check_password
import requests


class UserInfo(generics.RetrieveAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = UserSerializer

    def get_object(self):
        return self.request.user


class KakaoLogin(SocialLoginView):
    adapter_class = KakaoOAuth2Adapter

def set_kakao_params(auth_code):
    grant_type = "authorization_code"
    client_id = settings.CONF_FILES['kakao']['client_id']
    redirect_uri = "https://api.pycon.shop/user/res/"
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

def save_user_token(auth_key, access_params):
    user = Token.objects.get(key=auth_key['key'])
    user_ob = CustomUser.objects.get(id=user.user_id)
    user_ob.refresh_token = access_params['refresh_token']
    user_ob.access_key = access_params['access_token']
    user_ob.save()

def get_auth_token(access_token):
    data = {'access_token':access_token}
    req_url = "https://api.pycon.shop/rest-auth/kakao/"
    response = requests.post(req_url, data=data)
    response_dict = response.json()
    return response_dict

def kakao_oauth(request):
    try:
        auth_code = request.GET["code"]
        req_params = set_kakao_params(auth_code)
        access_token_params = get_access_token(req_params)
        access_token = access_token_params['access_token']
        auth_key = get_auth_token(access_token)
        save_user_token(auth_key, access_token_params)
        refer_url = 'https://app.pycon.shop/oauth'
        response = HttpResponseRedirect(refer_url, auth_key)
        response.set_cookie('token', auth_key['key'])
        return response
    except KeyError as err:
        return HttpResponse(err)

def empty_view(request, uidb64, token):
    reset_url = 'http://localhost:8080/pass-reset/' + uidb64 + '/' + token
    return HttpResponseRedirect(reset_url)
 
@api_view(["POST"])
def change_username(request):
    qs = CustomUser.objects.get(email=request.user)
    new_username = request.data['new_username']
    qs.username = new_username
    qs.save()
    return HttpResponse('')

@api_view(["POST"])
def membership_withdrawal(request):
    qs = CustomUser.objects.get(email=request.user)
    check_pw = request.data['check_pw']
    if check_password(check_pw, qs.password):
        qs.delete()
    else:
        return HttpResponse("check password", status=400)
    return HttpResponse("delete user")

# 가입 후 인증 메일에서 링크를 누르면 유저 정보 페이지로 리다이렉트 시킴
def redirect_view(request, key):
    return redirect('https://app.pycon.shop/UserInfo')