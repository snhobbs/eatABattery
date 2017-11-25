# -*- coding: utf-8 -*-
# Generated by Django 1.10.8 on 2017-11-24 03:29
from __future__ import unicode_literals

from django.db import migrations, models
import mezzanine.core.fields


class Migration(migrations.Migration):

    dependencies = [
        ('batteryPages', '0004_auto_20171117_0047'),
    ]

    operations = [
        migrations.CreateModel(
            name='AudioClip',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=75)),
                ('description', models.TextField()),
                ('mp3', mezzanine.core.fields.FileField(max_length=255, verbose_name='MP3')),
            ],
        ),
        migrations.DeleteModel(
            name='Case',
        ),
        migrations.RemoveField(
            model_name='patent',
            name='label',
        ),
        migrations.DeleteModel(
            name='Patent',
        ),
        migrations.DeleteModel(
            name='PatentGroup',
        ),
    ]
