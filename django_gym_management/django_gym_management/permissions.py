from rest_framework.permissions import BasePermission

class IsSuperUser(BasePermission):
    """
    Allows access only to superusers.
    """

    def has_permission(self, request, view):
        return request.user and request.user.is_superuser  # Only allow superusers

    def has_object_permission(self, request, view, obj):
        return request.user and request.user.is_superuser  # Object-level permission
