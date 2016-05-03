# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-04-29 23:30
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('uploadconvert', '0007_auto_20160429_2313'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movie',
            name='uploader',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, unique=True),
        ),
    ]