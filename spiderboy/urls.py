#coding=utf-8
from django.conf.urls import include, url, patterns
from django.contrib import admin
from django.conf.urls.static import static  
from django.conf import settings
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'testsite.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    #短路原理
    url(r'^', include('blog.urls')),
    #设置静态文件
    #url(r'^static/(?P<path>.*)$','django.views.static.serve',{'document_root':settings.STATIC_ROOT}),
) 
