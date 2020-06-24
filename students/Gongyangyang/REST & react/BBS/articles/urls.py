from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
router.register(r'articles', views.ArticleViewSet)
urlpatterns = [
    path('', include(router.urls)),
    # path('',views.index, name='index'),
    # path('<int:article_id>/', views.detail, name='detail'),
    # path('articles/create/', views.create, name='article_create'),
    # path('<int:question_id>/results/', views.results, name='results'),
    # path('<int:question_id>/vote/', views.vote, name='vote'),
]