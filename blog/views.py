from django.shortcuts import render
from django.views.generic import TemplateView

from .models import Blog, Category, Article

class BlogDetailView(TemplateView):
    template_name = 'blog_detail.html'

    def get_context_data(self, **kwargs):
        context = super(BlogDetailView, self).get_context_data(**kwargs)
        try:
            blog = Blog.objects.latest('id')
        except Blog.DoesNotExist:
            blog = Blog.objects.create(title='A Blog With No Name')
        context['blog'] = blog
        context['categories'] = Category.objects.all()
        context['article'] = Article.objects.latest('id')
        return context
