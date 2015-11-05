#coding=utf-8
from django.contrib import admin

# Register your models here.
from blog.models import Author, Article, Tag, Classification 

class AuthorAdmin(admin.ModelAdmin):
  list_display = ('name','email','website')
  #设置作者的类显示的表头
  search_field = ('name',)
  #添加按姓名查询的功能

class ArticleAdmin(admin.ModelAdmin):
  list_display = ('caption','id','author','publish_time','classification')
  list_filter = ('publish_time',)
  date_hierarchy = 'publish_time'
  #设置时间过滤器
  ordering = ('-publish_time',)
  filter_horizontal = ('tags',)
  #水平显示的过滤器
#以上为对显示内容的修饰
admin.site.register (Author, AuthorAdmin)
admin.site.register (Article, ArticleAdmin)
admin.site.register (Tag)
admin.site.register (Classification)


