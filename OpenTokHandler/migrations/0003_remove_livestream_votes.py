# -*- coding: utf-8 -*-
# Generated by Django 1.11.10 on 2018-03-11 05:17
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('OpenTokHandler', '0002_auto_20180311_0517'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='livestream',
            name='votes',
        ),
    ]