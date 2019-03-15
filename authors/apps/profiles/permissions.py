from rest_framework.permissions import BasePermission, SAFE_METHODS


class IsOwnerOrReadOnly(BasePermission):
    message = 'You are not the owner of this profile.'

    def has_permission(self, request, view):

        if request.method in SAFE_METHODS:
            return True
        username = view.kwargs.get('username')
        return request.user.username == username
