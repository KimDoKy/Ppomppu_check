from .models import CustomUser
from .serializers import UserSerializer
from allauth.socialaccount.providers.kakao.views import KakaoOAuth2Adapter
from rest_auth.registration.views import SocialLoginView
from rest_framework import generics


class UserInfo(generics.RetrieveAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = UserSerializer

    def get_object(self):
        return self.request.user


class KakaoLogin(SocialLoginView):
    adapter_class = KakaoOAuth2Adapter
