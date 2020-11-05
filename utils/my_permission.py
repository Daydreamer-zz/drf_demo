from rest_framework.permissions import BasePermission
from rest_framework import exceptions


class MyPermission(BasePermission):

    def has_permission(self, request, view):
        if request.user.user_type != 3:
            ret = dict()
            ret['code'] = 1004
            ret['message'] = '用户权限不足'
            raise exceptions.PermissionDenied(ret)
        return True
