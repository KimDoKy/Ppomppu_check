from rest_framework import generics
from rest_framework import permissions
from .models import Keywords
from .serializers import KeywordSerializer
from .permissions import IsOwner
from drf_yasg.utils import swagger_auto_schema


class KeywordCreateView(generics.CreateAPIView):
    """
    알림을 받을 키워드를 등록합니다.
    """
    queryset = Keywords.objects.all()
    serializer_class = KeywordSerializer 
    permission_classes = (permissions.IsAuthenticated,)

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class KeywordUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Keywords.objects.all()
    serializer_class = KeywordSerializer
    permission_classes = (permissions.IsAuthenticated, IsOwner)
    lookup_fields = ('keyword')

    def get():
        """
        키워드 상세 정보를 조회합니다. 
        """

    def put():
        """
        키워드를 수정하거나, 알람 여부를 변경합니다.  
        > keywords_partial_update의 사용을 권장합니다.
        """

    def patch():
        """
        키워드를 수정하거나, 알람 여부를 변경합니다. (권장)
        """

    def delete():
        """
        키워드를 삭제합니다.
        """
