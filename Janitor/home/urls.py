from django.conf.urls import patterns, url

from home import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
    url(r'^gadget/(?P<gadget_id>\d+)$', views.gadget_details, name='details'),
    url(r'^gadget/(?P<gadget_id>\d+)/do$', views.gadget_do, name='do'),
)
