from django.urls import path, include
from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from rest_framework.permissions import AllowAny
from . import rest_auth_url

schema_url_v1_patterns = [
    path('v1/users/', include('users.urls', namespace='users')),
    path('v1/keywords/', include('keywords.urls', namespace='keywords')),
    path('v1/rest-auth/', include(rest_auth_url, namespace='rest_auth')),
    ]

schema_view_v1 = get_schema_view(
    openapi.Info(
        title="User Info Api",
        default_version='v1',
        description="유저 정보 조회 API",
        contact=openapi.Contact(email="makingfunk0@gmail.com"),
        license=openapi.License(name="Makingfunk"),
        ),
    validators=['flex'],
    public=True,
    permission_classes=(AllowAny,),
    patterns=schema_url_v1_patterns,
    )
