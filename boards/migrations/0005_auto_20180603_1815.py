# -*- coding: utf-8 -*-
# Generated by Django 1.11.13 on 2018-06-03 18:15
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('boards', '0004_auto_20180510_1130'),
    ]

    operations = [
        migrations.AlterField(
            model_name='answer',
            name='media',
            field=models.FileField(upload_to='media/answers/'),
        ),
    ]
