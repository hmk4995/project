from django.conf.urls import url
from django.conf.urls import patterns, url
from .import  views 
from django.shortcuts import redirect



urlpatterns = [
    url(r'^/$', lambda _: redirect('admin:index')),
    url(r'^$', views.login, name='login'),
    url(r'^list/$', views.list, name='list'),
    url(r'^input/$', views.input, name='input'),
    url(r'^upload$', views.upload, name='upload'),
    
    
    
    
    #url(r'^question_list$', views.question_list, name='question_list'),
]



