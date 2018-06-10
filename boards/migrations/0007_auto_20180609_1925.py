# -*- coding: utf-8 -*-
# Generated by Django 1.11.13 on 2018-06-09 19:25
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('boards', '0006_auto_20180604_1940'),
    ]

    operations = [
        migrations.AddField(
            model_name='question',
            name='grade',
            field=models.IntegerField(blank=True, default=7),
        ),
        migrations.AlterField(
            model_name='question',
            name='media',
            field=models.ImageField(upload_to='questions'),
        ),
    ]
