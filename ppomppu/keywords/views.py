from rest_framework import generics
from rest_framework import permissions
from .models import Keywords
from .serializers import KeywordSerializer


class KeywordListView(generics.ListCreateAPIView):
    queryset = Keywords.objects.all()
    serializer_class = KeywordSerializer 
    permission_classes = (permissions.IsAuthenticated,)

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class KeywordUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Keywords.objects.all()
    serializer_class = KeywordSerializer
    permission_classes = (permissions.IsAuthenticated,)
    lookup_fields = ('keyword')
