from rest_framework.permissions import BasePermission
from .models import Post

class IsOwner(BasePermission):

    def has_object_permission(self, request, view, obj):
        if isinstance(obj, Post):
            return obj.author == request.user
        return obj.author == request.user
