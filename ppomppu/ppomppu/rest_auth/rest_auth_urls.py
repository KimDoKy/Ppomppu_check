from django.urls import path
from .rest_auth_views import RestLogin, RestLogout, RestUserDetails, RestPasswordChange, RestPasswordReset, RestPasswordResetConfirm

app_name = 'rest_auth'

urlpatterns = [
    path('login/', RestLogin.as_view(), name='rest_login'),
    path('logout/', RestLogout.as_view(), name='rest_logout'),
    path('user/', RestUserDetails.as_view(), name='rest_user_detail'),
    path('password/reset/', RestPasswordReset.as_view(), name='rest_password_reset'),
    path('password/reset/confirm/', RestPasswordResetConfirm.as_view(), name='rest_password_reset_confirm'),
    path('password/change/', RestPasswordChange.as_view(), name='rest_password_change'),
    ]
