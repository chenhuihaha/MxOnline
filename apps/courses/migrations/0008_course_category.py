# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2019-11-06 20:10
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0007_auto_20191106_1909'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='category',
            field=models.CharField(default='后端开发', max_length=50, verbose_name='课程类别'),
        ),
    ]