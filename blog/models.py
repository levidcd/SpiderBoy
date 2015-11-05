#_*_coding=utf-8_*_
from django.db import models

# Create your models here.

#作者
class Author(models.Model):
    name = models.CharField(max_length=25)
    email = models.EmailField(blank = True)
    website = models.URLField(blank=True)

    def __unicode__(self):
        return u'%s' %(self.name)
#标记
class Tag(models.Model):
    name = models.CharField(max_length=25)
    creat_time = models.DateTimeField(auto_now_add=True)

    def __unicode__(self):
        return u'%s' %(self.name)

#分类
class Classification(models.Model):
    name = models.CharField(max_length=25)

    def __unicode__(self):
        return u'%s' %(self.name)
#文章
class Article(models.Model):
    caption = models.CharField(max_length=50)
    author = models.ForeignKey(Author)
    tags = models.ManyToManyField(Tag,blank=True)
    classification = models.ForeignKey(Classification)
    content = models.TextField()
    publish_time = models.DateTimeField(auto_now_add=True)

    def __unicode__(self):
        return u'%s' %(self.caption)


    class Meta:
        ordering = ['-publish_time']
