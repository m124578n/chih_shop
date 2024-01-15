from rest_framework import permissions

class IsOwnerPermission(permissions.BasePermission):
    """
    check the user is the owner
    """

    def has_object_permission(self, request, view, obj):
        # Read permissions are allowed to any request,
        # so we'll always allow GET, HEAD, OPTIONS requests.
        if request.method in permissions.SAFE_METHODS:
            return True
        
        # obj here is a Product instance
        return obj.owner == request.user
    