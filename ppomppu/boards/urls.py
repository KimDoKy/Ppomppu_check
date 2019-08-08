from django.urls import path
from .views import CreateView, DetailView

urlpatterns = [
    path('posts/', CreateView.as_view(), name='create'),
    path('posts/<pk>/', DetailView.as_view(), name='detail'),
]
