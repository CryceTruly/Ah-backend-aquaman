from django.urls import path

from .views import (
    ArticlesApiView, ArticleDetailApiView,
    ArticleTagsApiView,
    ArticleLikeApiView, RateArticleView, ArticleLikeApiView,
)

urlpatterns = [
    path('articles/', ArticlesApiView.as_view(), name='articles'),
    path(
        'articles/<slug>/',
        ArticleDetailApiView.as_view(),
        name='article-detail'
    ),
    path(
        'articles/<slug>/like/',
        ArticleLikeApiView.as_view(),
        name='article-like'
    ),
    path("articles/<slug>/rate/", RateArticleView.as_view(), name="rating"),
    path(
        'tags/',
        ArticleTagsApiView.as_view(),
        name='article-tags'
    ),
]
