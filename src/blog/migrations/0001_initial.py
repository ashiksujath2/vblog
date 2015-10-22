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
                ('id', models.AutoField(auto_created=True, primary_key=True, verbose_name='ID', serialize=False)),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('updated_on', models.DateTimeField(auto_now=True)),
                ('title', models.CharField(unique=True, help_text='Title of the article', max_length=200)),
                ('slug', models.SlugField(unique=True, max_length=200)),
                ('abstract', models.TextField(null=True)),
                ('description', models.TextField()),
                ('is_published', models.BooleanField(default=False, help_text='Only Published Articles will appear in the blog')),
                ('published_date', models.DateTimeField(null=True, blank=True)),
            ],
            options={
                'ordering': ['-created_on'],
                'verbose_name_plural': 'Articles',
            },
        ),
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, verbose_name='ID', serialize=False)),
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
                ('id', models.AutoField(auto_created=True, primary_key=True, verbose_name='ID', serialize=False)),
                ('title', models.CharField(help_text='Title of the Blog', max_length=200)),
                ('logo', models.ImageField(null=True, help_text='Site Logo', upload_to='')),
                ('home_bgcolor', models.CharField(help_text='Background Color for homepage', max_length=20)),
                ('contact_bgcolor', models.CharField(help_text='Background Color for contact page', blank=True, max_length=20)),
                ('about_bgcolor', models.CharField(help_text='Background Color for about page', blank=True, max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, verbose_name='ID', serialize=False)),
                ('name', models.CharField(unique=True, max_length=30)),
                ('bg_color', models.CharField(blank=True, max_length=20)),
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
