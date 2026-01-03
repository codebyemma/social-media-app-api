from rest_framework.permissions import BasePermission

class IsOwner(BasePermission):
    """
    Allows access only to object owner.
    """

    def has_object_permission(self, request, view, obj):
        return obj.user == request.user

class IsCommentOwner(BasePermission):
    def has_object_permission(self, request, view, obj):
        return obj.user == request.user
