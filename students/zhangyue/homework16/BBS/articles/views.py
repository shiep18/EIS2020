from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from .forms import ArticlePostForm, LoginForm, UserRegisterForm
from .models import Article
from django.contrib.auth import authenticate, login, logout
from comment.models import Comment
from comment.forms import CommentForm
from django.contrib.auth.decorators import login_required
import markdown


def index(request):
    articles = Article.objects.all()
    return render(request, 'articles/index.html', context={'articles': articles})


def detail(request, pk):
    article = get_object_or_404(Article, pk=pk)
    article.body = markdown.markdown(article.body,
                                     extensions=[
                                         'markdown.extensions.extra',
                                         'markdown.extensions.fenced_code',
                                         'markdown.extensions.toc',
                                     ])
    comments = Comment.objects.filter(article=pk)
    comment_form = CommentForm()
    context = {'article': article, 'comments': comments, 'comment_form': comment_form}
    return render(request, 'articles/detail.html', context=context)


@login_required(login_url='/login/')
def create(request):
    if request.method == 'POST':
        article_post_form = ArticlePostForm(request.POST, request.FILES)

        if article_post_form.is_valid():
            new_article = article_post_form.save(commit=False)
            new_article.author = request.user
            new_article.save()
            return redirect("/")
        else:
            return HttpResponse("表单内容有误，请重新填写")
    else:
        article_post_form = ArticlePostForm()
        context = {'article_post_form': article_post_form}
        return render(request, 'articles/create.html', context)


def user_login(request):
    if request.method == 'POST':
        user_login_form = LoginForm(data=request.POST)
        if user_login_form.is_valid():
            # .cleaned_data 清洗出合法数据
            data = user_login_form.cleaned_data
            # 检验账号、密码是否正确匹配数据库中的某个用户
            # 如果均匹配则返回这个 user 对象
            user = authenticate(username=data['username'], password=data['password'])
            if user:
                # 将用户数据保存在 session 中，即实现了登录动作
                login(request, user)
                return redirect("/")
            else:
                return HttpResponse("账号或密码输入有误。请重新输入~")
        else:
            return HttpResponse("账号或密码输入不合法")
    elif request.method == 'GET':
        user_login_form = LoginForm()
        context = {'form': user_login_form}
        return render(request, 'articles/login.html', context)
    else:
        return HttpResponse("请使用GET或POST请求数据")


def user_logout(request):
    logout(request)
    return redirect("/")


def user_register(request):
    if request.method == 'POST':
        user_register_form = UserRegisterForm(data=request.POST)
        if user_register_form.is_valid():
            new_user = user_register_form.save(commit=False)
            # 设置密码
            new_user.set_password(user_register_form.cleaned_data['password'])
            new_user.save()
            # 保存好数据后立即登录并返回博客列表页面
            login(request, new_user)
            return redirect("/")
        else:
            return HttpResponse("注册表单输入有误。请重新输入~")
    elif request.method == 'GET':
        user_register_form = UserRegisterForm()
        context = {'form': user_register_form}
        return render(request, 'articles/register.html', context)
    else:
        return HttpResponse("请使用GET或POST请求数据")
