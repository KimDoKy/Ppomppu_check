from django.urls import path
from .views import CreateView

urlpatterns = [
    path('create/', CreateView.as_view(), name='create'),
]