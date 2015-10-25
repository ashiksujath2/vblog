from django.http import Http404
from django.views.generic import TemplateView

from .models import Blog, Category, Article, Author


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
        context['heading'] = blog.title
        context['header_bg_color'] = blog.home_bgcolor
        context['sub_heading'] = blog.sub_heading
        context['meta'] = ""
        return context


class HomeView(BaseMixin, TemplateView):
    template_name = 'blog/home.html'


class ArticleDetailView(BaseMixin, TemplateView):
    template_name = 'blog/detail.html'

    def get_category_meta(self, _category):
        d = {}
        d['heading'] = _category.name
        if _category.bg_color:
            d['header_bg_color'] = _category.bg_color
        d['sub_heading'] = _category.sub_heading if _category.sub_heading else ""
        return d

    def get_context_data(self, **kwargs):
        category_slug = kwargs.get('category_slug', '')
        article_slug = kwargs.get('article_slug', '')
        context = super(ArticleDetailView, self).get_context_data(**kwargs)
        article = Article.objects.get_article_by_category(
            category_slug,
            article_slug
        )
        if not article:
            raise Http404
        _category = Category.objects.get(slug=category_slug)
        context['article'] = article
        context.update(self.get_category_meta(_category))
        meta = 'Posted by <a href="#">{}</a> on {}'.format(
            article.author,
            article.published_date.strftime("%B %d, %Y") if article.published_date else article.published_date
        )
        context["meta"] = meta
        return context


class CategoryView(BaseMixin, TemplateView):
    template_name = 'blog/home.html'

    def get_category_meta(self, _category):
        d = {}
        d['heading'] = _category.name
        if _category.bg_color:
            d['header_bg_color'] = _category.bg_color
        d['sub_heading'] = _category.sub_heading if _category.sub_heading else ""
        return d

    def get_context_data(self, **kwargs):
        category_slug = kwargs.get('category_slug', '')
        context = super(CategoryView, self).get_context_data(**kwargs)
        _category = None
        try:
            _category = Category.objects.get(slug=category_slug)
        except Category.DoesNotExist:
            raise Http404
        context['category'] = _category
        context.update(self.get_category_meta(_category))
        return context


class AboutView(BaseMixin, TemplateView):
    template_name = 'blog/about.html'

    def get_context_data(self, **kwargs):
        try:
            author = Author.objects.latest('id')
        except Author.DoesNotExist:
            raise Http404
        context = super(AboutView, self).get_context_data(**kwargs)
        context['author'] = author
        context['heading'] = "About Me"
        if context['blog'].about_bgcolor:
            context['header_bg_color'] = context['blog'].about_bgcolor
        context['sub_heading'] = "This is what I do"
        return context


class ContactView(BaseMixin, TemplateView):
    template_name = 'blog/contact.html'

    def get_context_data(self, **kwargs):
        context = super(ContactView, self).get_context_data(**kwargs)
        context['heading'] = "Contact Me"
        if context['blog'].contact_bgcolor:
            context['header_bg_color'] = context['blog'].contact_bgcolor
        context['sub_heading'] = "Have questions? I have answers (maybe)."
        return context
