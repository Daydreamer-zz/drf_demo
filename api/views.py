from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.parsers import JSONParser
from api.models import UserInfo, UserToken
from utils.my_throttle import IpVisitThrottle
import uuid
import time


ORDER_DICT = {
    1:{
        'name': 'azhe',
        'age': 18,
        'gender': '男',
        'content': 'caonima'
    },
    2:{
        'name': 'dog',
        'age': 19,
        'gender': '男',
        'content': 'buhuib'
    },
}


# Create your views here.
class AuthView(APIView):
    """
    用户登录认证
    """
    parser_classes = [JSONParser]
    authentication_classes = []
    permission_classes = []
    throttle_classes = [IpVisitThrottle, ]

    def post(self, request, *args, **kwargs):
        ret = {'code': 1000, 'message': None}

        username = request.data['username']
        password = request.data['password']

        user = UserInfo.objects.filter(username=username).first()
        if user and user.verify_password(password):
            login_token_obj = UserToken.objects.filter(user=user).first()
            if not login_token_obj:
                token = uuid.uuid4().hex
                expire_in = time.time() + 3600
                UserToken.objects.create(user=user, token=token, expire_in=expire_in)
            else:
                token_isvalid = len(login_token_obj.token) == 32 and login_token_obj.expire_in >= time.time()
                token = login_token_obj.token if token_isvalid else uuid.uuid4().hex
                login_token_obj.token = token
                login_token_obj.expire_in = time.time() + 3600
                login_token_obj.save()
            ret['code'] = 1000
            ret['message'] = 'success'
            ret['token'] = token
            return Response(ret)
        ret['code'] = 1002
        ret['message'] = "用户名或密码错误"
        return Response(ret)


class OrderView(APIView):
    """
    返回实例订单接口测试
    """
    def get(self, request, *args, **kwargs):
        ret = {'code': 1000, 'message': None}
        try:
            ret['message'] = 'sucess'
            ret['data'] = ORDER_DICT
        except Exception as e:
            pass
        return Response(ret)
