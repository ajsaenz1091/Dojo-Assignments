from django.conf.urls import url
from . import views


urlpatterns = [
	url(r'^$', views.index),
	url(r'^register$', views.register),
	url(r'^welcome$', views.welcome),
	url(r'^logged$', views.login),
	url(r'^logout$', views.logout),
	url(r'^posts$', views.posts),
	url(r'^new_quote$', views.new_quote),
]