# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0002_product_amz_link'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='short_description',
            field=models.TextField(default='Short Description'),
            preserve_default=False,
        ),
    ]
