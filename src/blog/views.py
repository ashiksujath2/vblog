from django.http import Http404
from django.views.generic import TemplateView

from .models import Blog, Category, Article


class BaseMixin(object):
    """
    A default context mixin that loads common used context variables
    """

    def get_context_data(self, **kwargs):
        context = super(BaseMixin, self).get_context_data(**kwargs)
        try:
            blog = Blog.objects.latest('id')
        except Blog.DoesNotExist:
            blog = Blog.objects.create(title='Purely Binary', home_bgcolor="#000")
        context['blog'] = blog
        context['categories'] = Category.objects.all()
        return context


class HomeView(BaseMixin, TemplateView):
    template_name = 'blog/home.html'


class ArticleDetailView(BaseMixin, TemplateView):
    template_name = 'blog/detail.html'

    def get_context_data(self, **kwargs):
        category = kwargs.get('category_slug', '')
        article = kwargs.get('article_slug', '')
        context = super(ArticleDetailView, self).get_context_data(**kwargs)
        context['article'] = Article.objects.get_article_by_category(category, article)
        if not context['article']:
            raise Http404
        return context


class CategoryView(BaseMixin, TemplateView):
    template_name = 'blog/home.html'

    def get_context_data(self, **kwargs):
        category_slug = kwargs.get('category_slug', '')
        context = super(CategoryView, self).get_context_data(**kwargs)
        try:
            context['category'] = Category.objects.get(slug=category_slug)
        except Category.DoesNotExist:
            raise Http404
        return context

