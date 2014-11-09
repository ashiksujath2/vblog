from django.shortcuts import render

from django.views.generic import TemplateView


class BlogDetailView(TemplateView):
    template_name = 'blog_detail.html'
