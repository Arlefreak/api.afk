# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-03-21 23:36
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('diary', '0004_auto_20160307_0458'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='post',
            options={'ordering': ['dateCreated', 'order', 'title']},
        ),
    ]