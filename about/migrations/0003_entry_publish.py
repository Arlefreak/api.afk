# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-05-01 22:12
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('about', '0002_remove_entry_notes'),
    ]

    operations = [
        migrations.AddField(
            model_name='entry',
            name='publish',
            field=models.BooleanField(default=False),
        ),
    ]
