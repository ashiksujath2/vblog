# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='blog',
            options={'verbose_name': 'Purely Binary', 'verbose_name_plural': 'Purely Binary'},
        ),
        migrations.AddField(
            model_name='blog',
            name='sub_heading',
            field=models.CharField(help_text='Sub Heading of the Blog', blank=True, max_length=50),
        ),
        migrations.AddField(
            model_name='category',
            name='sub_heading',
            field=models.CharField(blank=True, max_length=50),
        ),
        migrations.AlterField(
            model_name='blog',
            name='logo',
            field=models.ImageField(upload_to='', help_text='Site Logo', blank=True, null=True),
        ),
    ]
