# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True, serialize=False)),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('updated_on', models.DateTimeField(auto_now=True)),
                ('title', models.CharField(max_length=300, unique=True, help_text='Title of the article')),
                ('slug', models.SlugField(max_length=300, unique=True)),
                ('abstract', models.TextField(null=True)),
                ('description', models.TextField()),
                ('is_published', models.BooleanField(help_text='Only Published Articles will appear in the blog', default=False)),
                ('published_date', models.DateTimeField(blank=True, null=True)),
            ],
            options={
                'ordering': ['-created_on'],
                'verbose_name_plural': 'Articles',
            },
        ),
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True, serialize=False)),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('updated_on', models.DateTimeField(auto_now=True)),
                ('first_name', models.CharField(max_length=100)),
                ('last_name', models.CharField(max_length=100)),
                ('about_me', models.TextField(blank=True)),
                ('user', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Author',
                'verbose_name_plural': 'Authors',
            },
        ),
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True, serialize=False)),
                ('title', models.CharField(max_length=300, help_text='Title of the Blog')),
                ('logo', models.ImageField(upload_to='', null=True, help_text='Site Logo')),
                ('home_poster', models.ImageField(upload_to='', help_text='Poster image for homepage')),
                ('contact_poster', models.ImageField(upload_to='', null=True, help_text='Poster image for contact page')),
                ('about_poster', models.ImageField(upload_to='', null=True, help_text='Poster image for about page')),
            ],
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True, serialize=False)),
                ('name', models.CharField(max_length=30, unique=True)),
                ('image', models.ImageField(null=True, upload_to='')),
                ('slug', models.SlugField()),
            ],
        ),
        migrations.AddField(
            model_name='article',
            name='author',
            field=models.ForeignKey(to='blog.Author'),
        ),
        migrations.AddField(
            model_name='article',
            name='category',
            field=models.ForeignKey(to='blog.Category'),
        ),
    ]
