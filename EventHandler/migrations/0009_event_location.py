# -*- coding: utf-8 -*-
# Generated by Django 1.11.10 on 2018-03-03 09:28
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('EventHandler', '0008_auto_20180302_1659'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='location',
            field=models.CharField(default='Cebu', max_length=50),
        ),
    ]
