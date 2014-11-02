from django.contrib import admin
from blog.models import Author, BlogEntry

class AuthorAdmin(admin.ModelAdmin):
    pass

class BlogEntryAdmin(admin.ModelAdmin):
    pass

admin.site.register(Author, AuthorAdmin)
admin.site.register(BlogEntry, BlogEntryAdmin)
