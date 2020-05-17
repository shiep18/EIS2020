from django.http import HttpResponse,HttpResponseRedirect
from django.template import loader
from django.shortcuts import get_object_or_404,render, redirect
from django.urls import reverse
from .forms import ArticlePostForm

from .models import Article

# Create your views here.

def index(request):
    latest_article_list = Article.objects.order_by('-pub_date')[::-1]
    context = {
        'latest_article_list': latest_article_list,
    }
    return render(request, 'articles/index.html',context)

def detail(request, article_id):
    article = get_object_or_404(Article,pk=article_id)
    return render(request, 'articles/detail.html',{'article':article})

def create(request):
    if request.method == 'POST':
        article_post_form = ArticlePostForm(request.POST, request.FILES)

        if article_post_form.is_valid():
            new_article = article_post_form.save(commit=False)
            new_article.save()
            return redirect("/articles/")
        else:
            return HttpResponse("表单内容有误，请重新填写")
    else:
        article_post_form = ArticlePostForm()
        context = {'article_post_form': article_post_form}
        return render(request, 'articles/create.html', context)