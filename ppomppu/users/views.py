from .models import CustomUser
from .serializers import UserSerializer
from rest_framework import generics


class UserInfo(generics.RetrieveAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = UserSerializer

    def get_object(self):
        return self.request.user



