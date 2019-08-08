from rest_framework import generics
from rest_framework import permissions
from .models import Keywords
from .serializers import KeywordSerializer
from .permissions import IsOwner

class KeywordCreateView(generics.CreateAPIView):
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
