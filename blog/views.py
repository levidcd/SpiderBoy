#coding=utf-8
from django.shortcuts import render_to_response,get_object_or_404
from django.template import RequestContext
from blog.models import Article,Tag,Classification
from django.http import Http404
from django.core.paginator import Paginator,PageNotAnInteger,EmptyPage
def index(request):
	articles = Article.objects.all()
	paginator = Paginator(articles,5)
	page_num = request.GET.get('page')
	try:
	 articles = paginator.page(page_num)
	except PageNotAnInteger:
	 articles = paginator.page(1)
	except EmptyPage:
	 articles = paginator.page(paginator.num_pages)
	classification = Classification.objects.all()
	return render_to_response('blog/index.html',
				  locals(),
				  context_instance=RequestContext(request))
def content(request, id):
	article = get_object_or_404(Article, id=id)
	classification = Classification.objects.all()
	return render_to_response('blog/content.html',
				  locals(),
				  context_instance=RequestContext(request))
def classification(request,id):
	try:
		cate = Classification.objects.get(id=id)
	except Classification.DoesNotExist:
		raise Http404
	is_category = True
	articles = Article.objects.filter(classification=cate)
	paginator = Paginator(articles,5)
	page_num = request.GET.get('page')
	try:
	 articles = paginator.page(page_num)
	except PageNotAnInteger:
	 articles = paginator.page(1)
	except EmptyPage:
	 articles = paginator.page(paginator.num_pages)
	classification = Classification.objects.all()
	return render_to_response('blog/index.html',
							  locals(),
				context_instance=RequestContext(request))