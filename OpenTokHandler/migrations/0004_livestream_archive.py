# -*- coding: utf-8 -*-
# Generated by Django 1.11.10 on 2018-03-21 10:07
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('OpenTokHandler', '0003_remove_livestream_votes'),
    ]

    operations = [
        migrations.AddField(
            model_name='livestream',
            name='archive',
            field=models.CharField(blank=True, default='', max_length=200),
        ),
    ]