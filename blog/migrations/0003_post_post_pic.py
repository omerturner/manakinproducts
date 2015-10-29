# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_auto_20151019_0933'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='post_pic',
            field=models.ImageField(default='media/no_image.png', upload_to='media/'),
        ),
    ]
