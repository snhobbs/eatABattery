# -*- coding: utf-8 -*-
# Generated by Django 1.10.8 on 2017-11-30 14:46
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('batteryPages', '0009_video_video'),
    ]

    operations = [
        migrations.AddField(
            model_name='video',
            name='description',
            field=models.TextField(default=''),
        ),
        migrations.AddField(
            model_name='video',
            name='title',
            field=models.CharField(default='', max_length=75),
        ),
    ]
