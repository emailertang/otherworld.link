# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-11-23 15:59
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('linkstart', '0003_auto_20171123_2358'),
    ]

    operations = [
        migrations.AlterField(
            model_name='index',
            name='content_1',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='index',
            name='content_2',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='index',
            name='content_3',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='index',
            name='content_4',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='index',
            name='content_5',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='index',
            name='content_6',
            field=models.TextField(null=True),
        ),
    ]
