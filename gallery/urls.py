# coding: utf-8
# Copyright (c) 2011-2012 Aymeric Augustin. All rights reserved.

from __future__ import unicode_literals

from django.conf.urls import patterns, url

from . import views


urlpatterns = patterns('',
    url(r'^$', views.GalleryIndexView.as_view(), name='index'),
    url(r'^year/(?P<year>\d{4})/$', views.GalleryYearView.as_view(), name='year'),
    url(r'^album/(?P<pk>\d+)/$', views.AlbumView.as_view(), name='album'),
    url(r'^photo/(?P<pk>\d+)/$', views.PhotoView.as_view(), name='photo'),
    url(r'^original/(?P<pk>\d+)/$', views.original_photo, name='photo-original'),
    url(r'^(?P<preset>\w+)/(?P<pk>\d+)/$', views.resized_photo, name='photo-resized'),
    url(r'^latest/$', views.latest_album, name='latest'),
)
