# -*- coding: utf-8 -*-

from django.urls import re_path

from .conf import settings
from . import views

L = settings.LIBPASTE_SLUG_LENGTH

urlpatterns = [
    re_path(r'^$', views.snippet_new, name='snippet_new'),
    re_path(r'^upload/$', views.snippet_upload, name='snippet_upload'),
    re_path(r'^diff/$', views.snippet_diff, name='snippet_diff'),
    re_path(r'^history/$', views.snippet_history, name='snippet_history'),
    re_path(r'^delete/$', views.snippet_delete, name='snippet_delete'),
    re_path(r'^api/$', views.snippet_api, name='api_create_snippet'),
    re_path(r'^(?P<snippet_id>[a-zA-Z0-9]{%d})/?$' % L, views.snippet_details, name='snippet_details'),
    re_path(r'^(?P<snippet_id>[a-zA-Z0-9]{%d})/delete/$' % L, views.snippet_delete, name='snippet_delete'),
    re_path(r'^(?P<snippet_id>[a-zA-Z0-9]{%d})/raw/?$' % L, views.snippet_details, {'template_name': 'libpaste/snippet_details_raw.html', 'is_raw': True}, name='snippet_details_raw'),
]
