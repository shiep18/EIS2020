from django.http import HttpResponse,HttpResponseRedirect, JsonResponse
from django.template import loader
from django.shortcuts import get_object_or_404,render, redirect
from django.urls import reverse
from .forms import ArticlePostForm

from rest_framework.parsers import JSONParser
from .serializers import ArticleSerializer
from django.views.decorators.csrf import csrf_exempt
from rest_framework import viewsets

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

# @csrf_exempt
# def article_list(request):
#     if request.method == 'GET':
#         articles = Article.objects.all()
#         serializer = ArticleSerializer(articles,many=True)
#         return JsonResponse(serializer.data, safe=False)

#     elif request.method == 'POST':
#         data = JSONParser().parse(request)
#         serializer = ArticleSerializer(data=data)
#         if serializer.is_valid():
#             serializer.save()
#             return JsonResponse(serializer.data, status=201)

#         return JsonResponse(serializer.errors, status=400)

# @csrf_exempt
# def article_detail(request, pk):
#     try:
#         article = Article.objects.get(pk=pk)
#     except Article.DoesNotExist:
#         return HttpResponse(status=404)

#     if request.method == 'GET':
#         serializer = ArticleSerializer(article)
#         return JsonResponse(serializer.data)

#     elif request.method == 'PUT':
#         data = JSONParser().parse(request)
#         serializer = ArticleSerializer(article, data=data)
#         if serializer.is_valid():
#             serializer.save()
#             return JsonResponse(serializer.data)
#         return JsonResponse(serializer.errors, status=400)

#     elif request.method == 'DELETE':
#         article.delete()
#         return HttpResponse(status=204)

class ArticleViewSet(viewsets.ModelViewSet):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer