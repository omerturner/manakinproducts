# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='WebsiteContact',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, auto_created=True, verbose_name='ID')),
                ('subject', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('message', models.CharField(max_length=100)),
            ],
        ),
    ]
