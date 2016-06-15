from django.conf.urls import url
from django.conf.urls import patterns, url
from .import  views 
from django.shortcuts import redirect



urlpatterns = [

    url(r'^$', views.login1, name='login1'),
    url(r'^listdis/$', views.listdis, name='listdis'),
    url(r'^loginauth/$', views.loginauth, name='loginauth'),
    url(r'^input/$', views.input, name='input'),
    url(r'^upload$', views.upload, name='upload'),
    
    
    
    
    #url(r'^question_list$', views.question_list, name='question_list'),
]



