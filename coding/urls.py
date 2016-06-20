from django.conf.urls import url
from django.conf.urls import patterns, url
from .import  views 
from django.shortcuts import redirect



urlpatterns = [

    url(r'^$', views.login1, name='login1'),
    url(r'^contest/(?P<cand>\w+?)/(?P<uname>\w+?)/', views.contest, name='contest'),
    url(r'^loginauth/$', views.loginauth, name='loginauth'),
    url(r'^input/$', views.input, name='input'),
    url(r'^upload$', views.upload, name='upload'),
    url(r'^final/$', views.final, name='final'),
    url(r'^listing/$', views.listing, name='listing'),
    url(r'^logout_candidate/$', views.logout_candidate, name='logout_candidate'),
    url(r'^ret/$', views.ret, name='ret')
    
    
    
    
    #url(r'^question_list$', views.question_list, name='question_list'),
]



