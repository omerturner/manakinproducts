# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_post_post_pic'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='link',
            field=models.CharField(max_length=100, blank=True),
        ),
        migrations.AddField(
            model_name='post',
            name='linkName',
            field=models.CharField(max_length=100, blank=True),
        ),
        migrations.AlterField(
            model_name='post',
            name='post_pic',
            field=models.ImageField(default=b'./no_image.png', upload_to=b''),
        ),
        migrations.AlterField(
            model_name='publisher',
            name='profile_pic',
            field=models.ImageField(default=b'./no_image.png', upload_to=b''),
        ),
    ]
