# -*- coding: utf-8 -*-
# Generated by Django 1.11.10 on 2018-03-25 09:36
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('OpenTokHandler', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='livestream',
            name='vote',
            field=models.IntegerField(default=0),
        ),
    ]