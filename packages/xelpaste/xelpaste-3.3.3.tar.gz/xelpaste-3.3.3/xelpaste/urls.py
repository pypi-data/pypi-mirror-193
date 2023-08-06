# -*- coding: utf-8 -*-

from django.urls import include, path

from . import views

urlpatterns = [
    path('about/', views.about, name='xelpaste_about'),
    path('', include('libpaste.urls')),
]
