# -*- coding: utf-8 -*-
# Generated by Django 1.10.8 on 2017-11-24 03:40
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('batteryPages', '0005_auto_20171124_0329'),
    ]

    operations = [
        migrations.CreateModel(
            name='AudioTag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.AddField(
            model_name='audioclip',
            name='tag',
            field=models.ManyToManyField(to='batteryPages.AudioTag'),
        ),
    ]
