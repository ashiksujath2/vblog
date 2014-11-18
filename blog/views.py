from django.http import Http404
from django.views.generic import TemplateView, ListView

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
            blog = Blog.objects.create(title='A Blog With No Name')
        context['blog'] = blog
        context['categories'] = Category.objects.all()
        return context


class ArticleDetailView(BaseMixin, TemplateView):
    template_name = 'article_detail.html'

    def get_context_data(self, **kwargs):
        category = kwargs.get('category_slug', '')
        article = kwargs.get('article_slug', '')
        context = super(ArticleDetailView, self).get_context_data(**kwargs)
        context['article'] = Article.objects.get_article_by_category(category, article)
        if not context['article']:
            raise Http404
        return context

class ArticleListView(BaseMixin, ListView):
    template_name = 'article_list.html'
    queryset = Article.objects.get_published_articles()
    context_object_name = 'article_list'
