# -*- coding: utf-8 -*-
# Generated by Django 1.11.10 on 2018-04-08 03:41
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('event', '0003_bookmark'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bookmark',
            name='is_bookmarked',
            field=models.BooleanField(default=True),
        ),
    ]
