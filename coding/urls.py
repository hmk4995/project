from django.conf.urls import url
from django.conf.urls import patterns, url
from .import  views 

urlpatterns = [
    url(r'^$', views.input, name='input'),
    url(r'^upload$', views.upload, name='upload'),
]



