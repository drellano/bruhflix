# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-04-29 21:46
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('uploadconvert', '0005_movie_title_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movie',
            name='title_slug',
            field=models.SlugField(default=b'', max_length=110),
        ),
    ]
