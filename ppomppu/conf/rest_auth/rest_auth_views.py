from rest_auth.views import LoginView, LogoutView, UserDetailsView, PasswordResetView, PasswordResetConfirmView, PasswordChangeView
from drf_yasg.utils import swagger_auto_schema
from rest_framework.decorators import api_view


class RestLogin(LoginView):
    """
    이메일 주소와 비밀번호로 로그인합니다.  
    로그인에 성공하면 토큰값을 반환합니다.  
    ```json
    {
        "key": "ljad23opidsdspdiop982jkjpd"
    }
    ```
    """

class RestLogout(LogoutView):
    """
    로그아웃을 합니다. 토큰을 헤더에 포함해야 backend 서버에서도 토큰이 삭제됩니다.  
    토큰을 포함하지 않아도 status 201으로 응답합니다.
    """

class RestUserDetails(UserDetailsView):
    """
    유저의 상세 정보를 반환합니다.
    """

class RestPasswordReset(PasswordResetView):
    """
    비밀번호를 분실했을때 유저의 이메일로 비밀번호 재설정 경로를 발송합니다.
    """

class RestPasswordResetConfirm(PasswordResetConfirmView):
    """
    비밀번호 분실로 인해 유저가 요청한 비밀번호 재설정 링크에서 비밀번호를 재설정합니다.
    """

class RestPasswordChange(PasswordChangeView):
    """
    비밀번호를 변경합니다.
    """
