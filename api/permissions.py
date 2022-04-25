from rest_framework import permissions


class OwnerOrReadOnly(permissions.BasePermission):

    def has_permission(self, request, view):
        return (
                request.method in permissions.SAFE_METHODS
                or (request.user.is_authenticated 
                    and request.user.user_role == 'Автор')
            )

    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        return (
                obj.author == request.user and 
                request.user.user_role == 'Автор'
            )
