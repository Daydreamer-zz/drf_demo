from rest_framework.throttling import BaseThrottle, SimpleRateThrottle


"""
import time
VISIT_RECORD = {}


class IpVisitThrottle(BaseThrottle):

    def __init__(self):
        self.history = None

    def allow_request(self, request, view):
        # 如果用户经过代理
        # if request.META.get('HTTP_X_FORWARDED_FOR'):
        #     ip = request.META.get('HTTP_X_FORWARDED_FOR')
        # else:
        #     ip = request.META.get('REMOTE_ADDR')
        ip = self.get_ident(request)
        now = time.time()

        # 某个IP第一次访问，不存在就添加以当前ip为key，当前时间戳为value，并直接返回允许
        if ip not in VISIT_RECORD:
            VISIT_RECORD[ip] = [now, ]
            return True

        # 从VISIT_RECORD字典取出当前ip的访问时间列表，并依次将当前时间从右向左插入
        history = VISIT_RECORD[ip]
        history.insert(0, now)

        # 确保当前ip的访问时间列表，最新的时间和最老的时间相差60s，超过60s的依次从列表剔除一个最早时间
        while history and history[0] - history[-1] > 60:
            history.pop()
            print('poped a time')

        self.history = history

        print(history)
        # 判断列表长度，是否符合60s内访问的次数
        if len(history) > 3:
            return False
        else:
            return True

    def wait(self):
        wait_time = 60 - (self.history[0] - self.history[-1])
        return wait_time
"""


class IpVisitThrottle(SimpleRateThrottle):

    scope = 'Wdnmd'

    # 使用drf内置的限流方法，必须重写get_cache_key方法
    def get_cache_key(self, request, view):
        return self.get_ident(request)


class UserThrottle(SimpleRateThrottle):

    scope = 'WdnmdUser'

    def get_cache_key(self, request, view):
        return request.user.username
