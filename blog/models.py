from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class BaseModel(models.Model):
    """Things which we always need to keep track of."""
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True

class Author(BaseModel):
    user = models.ForeignKey(User)
    about = models.TextField(blank=True)


    class Meta:
        verbose_name = 'Author'
        verbose_name_plural = 'Authors'

    def __unicode__(self):
        return self.user.get_full_name()


class BlogEntry(BaseModel):
    title = models.CharField(max_length=300, help_text='Title of the article')
    slug = models.SlugField(max_length=300)
    abstract = models.TextField(null=True)
    description = models.TextField()
    author = models.ForeignKey(Author)
    is_published = models.BooleanField(default=False, help_text='Only Published Entries will appear in the blog')
    published_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        ordering = ['-created_on']
        verbose_name_plural = 'Blog Entries'

    def __unicode__(self):
        return self.title

class Category(models.Model):
    name = models.CharField(max_length=30, unique=True)
    slug = models.SlugField()

    def __unicode__(self):
        return self.name
