# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', serialize=False, auto_created=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('title', models.CharField(max_length=255)),
                ('description', models.TextField()),
                ('image', models.ImageField(upload_to='media/', default='media/no_image.png')),
                ('image2', models.ImageField(upload_to='media/', default='media/no_image.png')),
                ('image3', models.ImageField(upload_to='media/', default='media/no_image.png')),
                ('image4', models.ImageField(upload_to='media/', default='media/no_image.png')),
                ('image5', models.ImageField(upload_to='media/', default='media/no_image.png')),
                ('image6', models.ImageField(upload_to='media/', default='media/no_image.png')),
            ],
        ),
    ]
