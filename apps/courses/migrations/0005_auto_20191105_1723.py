# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2019-11-05 17:23
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0004_auto_20191105_1721'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='image',
            field=models.ImageField(default='', upload_to='courses/%Y/%m', verbose_name='封面图'),
        ),
    ]
