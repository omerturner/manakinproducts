# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-01-10 10:32
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0011_auto_20151221_0135'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='slug',
            field=models.SlugField(default='slug'),
            preserve_default=False,
        ),
    ]
