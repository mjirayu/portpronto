from django.shortcuts import render
from django.http import HttpResponse, Http404
from articles.models import Article
from django.shortcuts import get_object_or_404


def index(request):
    lastest_article_list_2010 = Article.objects.order_by('year').filter(year="2010")
    lastest_article_list_2011 = Article.objects.order_by('year').filter(year="2011")
    lastest_article_list_2012 = Article.objects.order_by('year').filter(year="2012")
    lastest_article_list_2013 = Article.objects.order_by('year').filter(year="2013")
    lastest_article_list_2014 = Article.objects.order_by('year').filter(year="2014")
    lastest_article_list_2015 = Article.objects.order_by('year').filter(year="2015")

    context = {'lastest_article_list_2010': lastest_article_list_2010,
                'lastest_article_list_2011': lastest_article_list_2011,
                'lastest_article_list_2012': lastest_article_list_2012,
                'lastest_article_list_2013': lastest_article_list_2013,
                'lastest_article_list_2014': lastest_article_list_2014,
                'lastest_article_list_2015': lastest_article_list_2015,
    }
    return render(request, 'articles/index.html', context)


def detail(request, article_id):
    article = get_object_or_404(Article, pk=article_id)
    return render(request, 'articles/detail.html', {'article': article})

