# -*- coding: utf-8 -*-
# Generated by Django 1.11.10 on 2018-03-25 09:37
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('OpenTokHandler', '0002_livestream_vote'),
    ]

    operations = [
        migrations.RenameField(
            model_name='livestream',
            old_name='vote',
            new_name='votes',
        ),
    ]