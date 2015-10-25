import re
from django import template
from django.core.urlresolvers import reverse, NoReverseMatch

register = template.Library()

from blog.models import Article


@register.simple_tag(takes_context=True)
def active(context, pattern_or_urlname):
    try:
        pattern = reverse(pattern_or_urlname)
    except NoReverseMatch:
        pattern = pattern_or_urlname
    path = context['request'].path
    if re.search(pattern, path):
        return 'highlight'
    return ''


@register.inclusion_tag('blog/inclusion/article_box.html')
def article_box(category=None, limit=5):
    context = {}
    if category:
        context['articles'] = Article.objects.get_category_articles(category, limit=limit)
    else:
        context['articles'] = Article.objects.get_published_articles(limit=limit)
    return context
