from django.urls import path
from rest_auth.views import LoginView, LogoutView, UserDetailsView, PasswordChangeView, PasswordResetView, PasswordResetConfirmView

app_name = 'rest_auth'

urlpatterns = [
    path('login/', LoginView.as_view(), name='rest_login'),
    path('logout/', LogoutView.as_view(), name='rest_logout'),
    path('user/', UserDetailsView.as_view(), name='rest_user_detail'),
    path('password/reset/confirm/', PasswordResetConfirmView.as_view(), name='rest_password_reset_confirm'),
    path('password/change/', PasswordChangeView.as_view(), name='rest_password_change'),
    path('password/reset/', PasswordResetView.as_view(), name='rest_password_reset'),
    ]
