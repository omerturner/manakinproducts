# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2015-12-21 09:35
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0010_product_sale_price'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='price',
            field=models.FloatField(default=999.9),
        ),
        migrations.AlterField(
            model_name='product',
            name='sale_price',
            field=models.FloatField(default=999.9),
        ),
    ]
