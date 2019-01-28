from django.urls import include, path
from rest_framework.authtoken import views

urlpatterns = [
    path('users/', include('users.urls')),
    path('crawling/', include('crawling_data.urls')),
    path('rest-auth/', include('rest_auth.urls')),
    path('get-token/', views.obtain_auth_token),
#    path('rest-auth/registration/', include('rest_auth.registration.urls')),
    ]
