#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from rest_framework.authentication import BaseAuthentication
from rest_framework.authentication import exceptions
from api.models import UserInfo, UserToken
import time


class TokenAuthentication(BaseAuthentication):
    def authenticate(self, request):
        ret = {'code': None, 'message': None}
        token = request.META.get('HTTP_X_TOKEN')
        if not token:
            ret['code'] = 1001
            ret['message'] = '请求头错误'
            raise exceptions.AuthenticationFailed(ret)
        token_obj = UserToken.objects.filter(token=token).first()
        if not token_obj or token_obj.expire_in < time.time():
            ret['code'] = 1003
            ret['message'] = 'token过期或不存在，请重新登录'
            raise exceptions.AuthenticationFailed(ret)
        token_obj.expire_in = time.time() + 3600
        token_obj.save()
        user = token_obj.user
        return (user, None)

