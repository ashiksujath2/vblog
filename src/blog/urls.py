from django.conf.urls import url

from .views import HomeView, CategoryView, ArticleDetailView, AboutView, ContactView


urlpatterns = [
    url(r'^$', HomeView.as_view(), name="home"),
    url(r'^about$', AboutView.as_view(), name="about"),
    url(r'^contact$', ContactView.as_view(), name="contact"),
    url(r'^(?P<category_slug>.+)/(?P<article_slug>.+)/$',
        ArticleDetailView.as_view(), name='article_detail'),
    url(r'^(?P<category_slug>.+)$',
        CategoryView.as_view(), name='category_view'),
]
