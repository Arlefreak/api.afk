# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-05-30 23:28
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('podcast', '0014_auto_20170530_2217'),
    ]

    operations = [
        migrations.AddField(
            model_name='episode',
            name='small_text',
            field=models.CharField(default=1, max_length=255),
            preserve_default=False,
        ),
    ]
