from rest_framework.permissions import BasePermission


class IsLoggedInOrReadOnly(BasePermission):
    def has_permission(self, request, view):
        if request.method == "GET":
            return True

        return request.user is not None and request.user.is_authenticated