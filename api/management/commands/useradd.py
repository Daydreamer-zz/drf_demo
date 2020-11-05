#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from django.core.management.base import BaseCommand
from api.models import UserInfo


class Command(BaseCommand):
    help = '创建用户'

    def add_arguments(self, parser):
        parser.add_argument('-u', required=True, metavar='username', help='账户名')
        parser.add_argument('-p', required=True, metavar='password', help='密码')
        parser.add_argument('-t', required=False, metavar='user_type', help="用户类型")

    def handle(self, *args, **options):
        if UserInfo.objects.filter(username=options['u']).exists():
            return self.stderr.write(self.style.ERROR(f'已经存在用户名为【{options["u"]}】的用户'))
        UserInfo.objects.create(
            username=options['u'],
            password_hash=UserInfo.make_password(options['p']),
            user_type=options['t']
        )
        self.stdout.write(self.style.SUCCESS('创建用户成功'))
