#coding=utf-8
from django.conf.urls import patterns,url
from blog import views
from django.conf.urls.static import static
from django.conf import settings
from django.contrib import admin
admin.autodiscover()
#from views import local

urlpatterns = patterns('',
    url(r'^$','blog.views.index'),
    url(r'^article/(?P<id>\d+)/$','blog.views.content'),
    url(r'category/(?P<id>\d+)/$','blog.views.classification'),
    
)
#配置静态文件映射
if settings.DEBUG:
    urlpatterns += patterns('django.contrib.staticfiles.views',
        url(r'^static/(?P<path>.*)$', 'serve'),
    )