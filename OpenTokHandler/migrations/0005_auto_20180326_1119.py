# -*- coding: utf-8 -*-
# Generated by Django 1.11.10 on 2018-03-26 03:19
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('OpenTokHandler', '0004_auto_20180326_1118'),
    ]

    operations = [
        migrations.AlterField(
            model_name='viewer',
            name='livestream',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='viewers', to='OpenTokHandler.Livestream'),
        ),
        migrations.AlterField(
            model_name='viewer',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='viewers', to=settings.AUTH_USER_MODEL),
        ),
    ]