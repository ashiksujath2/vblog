from django.conf.urls import patterns, include, url

from blog.views import ArticleDetailView, ArticleListView, CategoryView


urlpatterns = patterns('',
    url(r'^$', ArticleListView.as_view(), name='article_list'),
    url(r'^(?P<category_slug>[a-zA-Z0-9_-]+)$',
        CategoryView.as_view(), name='category_view'),
    url(r'^(?P<category_slug>[a-zA-Z0-9_-]+)/(?P<article_slug>[a-zA-Z0-9_-]+)/$',
        ArticleDetailView.as_view(), name='article_detail'),
)
