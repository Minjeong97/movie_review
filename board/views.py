from django.shortcuts import render, redirect, get_object_or_404
from .models import Article
from .forms import ArticleForm


def detail (request, article_pk):
    article  = get_object_or_404(Article, pk=article_pk)
    context = {'article': article}
    return render(request, 'board/detail.html', context)

def create(request):
    if request.method == 'POST':
        article_form = ArticleForm(request.POST)
        if article_form.is_valid():
            article = article_form.save()
            return redirect('board:detail', article.pk)
          
    elif request.method == 'GET':
        article_form = ArticleForm()


    context = {'article_form': article_form, }
    return render(request, 'board/form_new.html', context)