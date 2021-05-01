from rest_framework import permissions


class IsAdminUser(permissions.BasePermission):
    """
    Global permission check for admin users.
    """

    def has_permission(self, request, view):
        user = request.user.is_superuser
        return user


class IsStaff(permissions.BasePermission):
    """
    Global permission check for staff users.
    """

    def has_permission(self, request, view):
        user = request.user.is_staff
        return user
