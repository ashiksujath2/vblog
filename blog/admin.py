from django.contrib import admin
from blog.models import Author, BlogEntry, Category

class AuthorAdmin(admin.ModelAdmin):
    pass

class BlogEntryAdmin(admin.ModelAdmin):
    pass

class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("name",)}


admin.site.register(Author, AuthorAdmin)
admin.site.register(BlogEntry, BlogEntryAdmin)
admin.site.register(Category, CategoryAdmin)
