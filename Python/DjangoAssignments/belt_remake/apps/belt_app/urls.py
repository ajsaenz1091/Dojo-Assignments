from django.conf.urls import url
from . import views

urlpatterns = [
	url(r'^welcome$', views.welcome),
	url(r'^logout$', views.logout),
	url(r'^posts$', views.posts),
	# url(r'^new_quote$', views.quote),


]