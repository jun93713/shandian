from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^neworder$', views.newOrderPage),
    url(r'^create$', views.create),
    url(r'^(?P<id>\d+)/manage$', views.managePage),
    url(r'^(?P<id>\d+)/delete$', views.remove),
    url(r'^(?P<id>\d+)/update$', views.updateOne),
    url(r'^history$', views.showAll),
    url(r'^search$', views.search),
]
