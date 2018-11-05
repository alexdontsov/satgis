from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from django.shortcuts import render

#######################################################################################################################
# Main page view
#######################################################################################################################
from app.models import Article


def index(request, template_name='index.html'):
    articles = Article.objects.all().order_by('-id')
    paginator = Paginator(articles, 2)
    page = request.GET.get('page')
    try:
        articles = paginator.page(page)
    except PageNotAnInteger:
        articles = paginator.page(1)
    except EmptyPage:
        articles = paginator.page(paginator.num_pages)

    return render(request, template_name, {'articles': articles})

def about(request, template_name='about.html'):
    return render(request, template_name)

def examples(request, template_name='examples.html'):
    return render(request, template_name)

def news(request, template_name='news.html'):
    articles = Article.objects.all().order_by('-id')
    paginator = Paginator(articles, 12)
    page = request.GET.get('page')

    try:
        articles = paginator.page(page)
    except PageNotAnInteger:
        articles = paginator.page(1)
    except EmptyPage:
        articles = paginator.page(paginator.num_pages)

    return render(request, template_name, {'articles': articles})
