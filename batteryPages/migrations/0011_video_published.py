# -*- coding: utf-8 -*-
# Generated by Django 1.10.8 on 2017-11-30 15:36
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('batteryPages', '0010_auto_20171130_1446'),
    ]

    operations = [
        migrations.AddField(
            model_name='video',
            name='published',
            field=models.DateTimeField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
