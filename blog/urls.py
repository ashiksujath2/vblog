from django.conf.urls import patterns, include, url

from blog.views import BlogDetailView


urlpatterns = patterns('',
    url(r'^$', BlogDetailView.as_view(), name='blog_detail'),
)
