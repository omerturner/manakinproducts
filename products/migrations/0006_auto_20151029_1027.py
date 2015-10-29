# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0005_auto_20151025_1354'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='order',
            field=models.IntegerField(default=999),
        ),
        migrations.AlterField(
            model_name='product',
            name='image',
            field=models.ImageField(default=b'./no_image.png', upload_to=b''),
        ),
        migrations.AlterField(
            model_name='product',
            name='image2',
            field=models.ImageField(default=b'./no_image.png', upload_to=b''),
        ),
        migrations.AlterField(
            model_name='product',
            name='image3',
            field=models.ImageField(default=b'./no_image.png', upload_to=b''),
        ),
        migrations.AlterField(
            model_name='product',
            name='image4',
            field=models.ImageField(default=b'./no_image.png', upload_to=b''),
        ),
        migrations.AlterField(
            model_name='product',
            name='image5',
            field=models.ImageField(default=b'./no_image.png', upload_to=b''),
        ),
        migrations.AlterField(
            model_name='product',
            name='image6',
            field=models.ImageField(default=b'./no_image.png', upload_to=b''),
        ),
    ]
