from django.urls import path

from . import views

app_name = 'articles'
urlpatterns = [
    path('',views.index, name='index'),
    path('<int:article_id>/', views.detail, name='detail'),
    path('articles/create/', views.create, name='article_create'),
    # path('<int:question_id>/results/', views.results, name='results'),
    # path('<int:question_id>/vote/', views.vote, name='vote'),
]