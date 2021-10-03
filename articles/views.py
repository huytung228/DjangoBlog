from django.shortcuts import redirect, render
from .models import Article
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from .forms import ArticleForm

# Create your views here.
@login_required(login_url="/accounts/login/")
def article_list(request):
    list_articles = Article.objects.all().order_by('date')
    return render(request, 'articles/article_list.html', {'arts' : list_articles})

def article_detail(request, slug_article):
    article = Article.objects.get(slug=slug_article)
    return render(request, 'articles/article_detail.html', {'article' : article})

def article_delete(request, article_delete):
    article = Article.objects.get(slug=article_delete)
    if request.method == 'POST':
        if 'yes' in request.POST:
            article.delete()
            return redirect('articles:list')
        if 'cancel' in request.POST:
            return redirect('../')
    return render(request, 'articles/article_delete.html', {'art' : article})

def article_edit(request, article_edit):
    article = Article.objects.get(slug=article_edit)
    if request.method == 'POST':
        f = ArticleForm(request.POST, request.FILES, instance=article)
        if f.is_valid():
            f.save()
            return redirect('articles:detail', article_edit)
    data = {
        'title' : article.title,
        'slug' : article.slug,
        'body' : article.body,
        'thumb' : article.thumb
    }
    f = ArticleForm(data)
    return render(request, 'articles/article_create.html', {'form' : f, 'action_type' : 'edit'})

@login_required(login_url="/accounts/login/")
def create_article(request):
    if request.method == 'POST':
        f = ArticleForm(request.POST, request.FILES)
        if f.is_valid():
            instance = f.save(commit=False)
            instance.author = request.user
            instance.save()
            return redirect('articles:list')
    f = ArticleForm()
    return render(request, 'articles/article_create.html', {'form' : f, 'action_type' : 'create'})