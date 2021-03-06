# -*- coding: utf-8 -*-

from django.conf.urls import url
from images import views as images_views

app_name = 'images'
urlpatterns = [
	url(r'^$', images_views.image_list, name = 'list'),
	url(r'^create/$', images_views.image_create, name = 'create'),
	url(r'^detail/(?P<id>\d+)/(?P<slug>[-\w]+)/$', images_views.image_detail, name = 'detail'),
	url(r'^like/$', images_views.image_like, name = 'like'),
	url(r'^ranking/$', images_views.image_ranking, name = 'ranking'),
]

