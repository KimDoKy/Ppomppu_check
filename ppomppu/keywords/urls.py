from django.urls import path
from .views import KeywordListView, KeywordUpdateDestroyView

urlpatterns = [
    path('', KeywordListView.as_view()),
    path('<pk>/', KeywordUpdateDestroyView.as_view()),
    ]
