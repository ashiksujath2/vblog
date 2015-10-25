from datetime import datetime

from django.db import models
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse


class BaseModel(models.Model):
    """Things which we always need to keep track of."""
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Blog(models.Model):
    """ Blog wide settings """
    title = models.CharField(max_length=200, help_text='Title of the Blog')
    sub_heading = models.CharField(max_length=50, blank=True, help_text='Sub Heading of the Blog')
    logo = models.ImageField(null=True, blank=True, help_text='Site Logo')
    home_bgcolor = models.CharField(max_length=20, help_text='Background Color for homepage')
    contact_bgcolor = models.CharField(max_length=20, blank=True, help_text='Background Color for contact page')
    about_bgcolor = models.CharField(max_length=20, blank=True, help_text='Background Color for about page')

    class Meta:
        verbose_name = 'Purely Binary'
        verbose_name_plural = 'Purely Binary'

    def __str__(self):
        return self.title


class Author(BaseModel):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    user = models.ForeignKey(User)
    about_me = models.TextField(blank=True)

    class Meta:
        verbose_name = 'Author'
        verbose_name_plural = 'Authors'

    def __str__(self):
        return "{} {}".format(self.first_name, self.last_name)


class Category(models.Model):
    name = models.CharField(max_length=30, unique=True)
    sub_heading = models.CharField(max_length=50, blank=True)
    bg_color = models.CharField(max_length=20, blank=True)
    slug = models.SlugField()

    def __str__(self):
        return self.name

    def get_url(self):
        return reverse('category_view', args=[self.slug])


class ArticleManager(models.Manager):

    def get_published_articles(self, limit=None):
        q = self.filter(is_published=True, published_date__lte=datetime.now()).order_by('published_date')
        if limit:
            return q[:int(limit)]
        return q

    def get_category_articles(self, category, limit=None):
        if not category:
            return []
        q = self.get_published_articles().filter(category__slug=category).order_by('published_date')
        if limit:
            return q[:int(limit)]
        return q

    def get_article_by_category(self, category, article):
        if not (category and article):
            return []
        try:
            return self.get_category_articles(category).get(slug=article)
        except Article.DoesNotExist:
            return []


class Article(BaseModel):
    title = models.CharField(max_length=200, help_text='Title of the article', unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    abstract = models.TextField(null=True)
    description = models.TextField()
    author = models.ForeignKey(Author)
    category = models.ForeignKey(Category)
    is_published = models.BooleanField(default=False, help_text='Only Published Articles will appear in the blog')
    published_date = models.DateTimeField(blank=True, null=True)

    objects = ArticleManager()

    class Meta:
        ordering = ['-created_on']
        verbose_name_plural = 'Articles'

    def __str__(self):
        return self.title

    @property
    def get_author(self):
        return self.author

    def get_url(self):
        return reverse('article_detail', args=[self.category.slug, self.slug])
