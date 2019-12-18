from django.urls import path, include
from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from rest_framework.permissions import AllowAny
from .rest_auth import rest_auth_urls

schema_url_v1_patterns = [
    path('users/', include('users.urls', namespace='users')),
    path('rest-auth/', include(rest_auth_urls, namespace='rest_auth')),
    path('keywords/', include('keywords.urls', namespace='keywords')),
    ]

schema_view_v1 = get_schema_view(
    openapi.Info(
        title="Ppomppu Backend Api",
        default_version='v1',
        description="PpomPpu Checker Backend API Docu #[app](https://app.pycon.shop)",
        contact=openapi.Contact(email="makingfunk0@gmail.com"),
        license=openapi.License(name="Makingfunk"),
        ),
    validators=['flex'],
    public=True,
    permission_classes=(AllowAny,),
    patterns=schema_url_v1_patterns,
    )
