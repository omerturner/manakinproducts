# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='amz_link',
            field=models.URLField(default='http://www.amazon.com/', max_length=255),
            preserve_default=False,
        ),
    ]
