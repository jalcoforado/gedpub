from rest_framework.permissions import BasePermission

class IsFromSameSetor(BasePermission):
    def has_object_permission(self, request, view, obj):
        return request.user.setor == obj.setor
