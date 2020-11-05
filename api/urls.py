#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from django.urls import path
from api import views

urlpatterns = [
    path('auth/', views.AuthView.as_view()),
    path('order/', views.OrderView.as_view())
]