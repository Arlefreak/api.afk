# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-09-04 11:17
from __future__ import unicode_literals

from django.db import migrations, models
import location_field.models.plain


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='City',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('city', models.CharField(max_length=255)),
                ('location', location_field.models.plain.PlainLocationField(max_length=63)),
                ('date_init', models.DateField()),
                ('date_final', models.DateField()),
            ],
        ),
    ]
