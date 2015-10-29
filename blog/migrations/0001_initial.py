# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(unique=True, max_length=100)),
                ('body', models.TextField()),
                ('posted', models.DateTimeField(auto_now_add=True, db_index=True)),
            ],
        ),
    ]
