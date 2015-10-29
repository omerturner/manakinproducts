# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Publisher',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(unique=True, max_length=25)),
                ('profile_pic', models.ImageField(upload_to='media/', default='media/no_image.png')),
            ],
        ),
        migrations.AddField(
            model_name='post',
            name='publisher',
            field=models.ForeignKey(to='blog.Publisher', default=1),
            preserve_default=False,
        ),
    ]
