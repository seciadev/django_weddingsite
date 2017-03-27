from django.conf.urls import url
from . import views

urlpatterns = [
	url(r'^$', views.welcome, name='index'),
	url(r'^villa/$', views.villa, name='villa'),
	url(r'^chiesa/$', views.chiesa, name='chiesa'),
	url(r'^conferma/$', views.conferma, name='conferma'),
	url(r'^regalo/$', views.regalo, name='regalo'),
	url(r'^grazie/$', views.grazie, name='grazie'),
]