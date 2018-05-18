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
    url(r'^purchaselist$', views.plist),
    url(r'^shoplist$', views.slist),
    url(r'^about$', views.about),
    url(r'^groupPurchase$', views.groupPurchase),
    url(r'^groupShip$', views.groupShip),
    url(r'^groupDelete$', views.groupDelete),

]
