#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from rest_framework import serializers
from api.models import UserInfo


class UserListSerializer(serializers.ModelSerializer):

    class Meta:
        model = UserInfo
        fields = ['id', 'username', 'user_type']
