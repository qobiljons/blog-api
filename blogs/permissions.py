from rest_framework import permissions


# class IsAuthorOrReadOnly(permissions.BasePermission):
#     def has_permission(self, request, view):
#         if request.method in permissions.SAFE_METHODS:
#             return True
        
#         if request.user and request.user.is_authenticated:
#             return hasattr(request.user, 'author')
        
#         return False
    
#     def has_object_permission(self, request, view, obj):
#         return obj.author == request.user
    


# class IsAuthor(permissions.BasePermission):
#     def has_permission(self, request, view):
#         if request.user and request.user.is_authenticated:
#             return hasattr(request.user, 'author')

#     def has_object_permission(self, request, view, obj):
#         return obj.author == request.user
  
class IsOwnerOrReadOnly(permissions.BasePermission):
    def has_permission(self, request, view):
        # Allow read-only methods for all users
        if request.method in permissions.SAFE_METHODS:
            return True
        # Allow other methods only if the user is authenticated
        return request.user and request.user.is_authenticated

    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        if request.method in ["DELETE", "PUT"]:
            return obj.author == request.user.author
        return False
    

class IsAdminOrReadOnly(permissions.BasePermission):
    def has_permission(self, request, view):
        return bool(
            request.method in permissions.SAFE_METHODS or
            request.user and
            request.user.is_staff
        )

class IsAuthorOrReadOnly(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.method in permissions.SAFE_METHODS:
            return True
        return request.user and request.user.is_authenticated 

    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        return obj.user == request.user