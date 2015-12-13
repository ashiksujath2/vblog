from django.contrib import admin
from blog.models import Author, Article, Category, Blog


class AuthorAdmin(admin.ModelAdmin):
    pass


class BlogAdmin(admin.ModelAdmin):
    pass


class ArticleAdmin(admin.ModelAdmin):
    change_form_template = 'blog/admin/change_form.html'
    prepopulated_fields = {"slug": ("title",)}


class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("name",)}


admin.site.register(Blog, BlogAdmin)
admin.site.register(Author, AuthorAdmin)
admin.site.register(Article, ArticleAdmin)
admin.site.register(Category, CategoryAdmin)
