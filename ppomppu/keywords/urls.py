from django.urls import path
from .views import KeywordCreateView, KeywordUpdateDestroyView

urlpatterns = [
    path('', KeywordCreateView.as_view()),
    path('<pk>/', KeywordUpdateDestroyView.as_view()),
    ]
