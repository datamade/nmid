# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-09-02 14:14
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('camp_fin', '0024_auto_20160831_0949'),
    ]

    operations = [
        migrations.AlterField(
            model_name='candidate',
            name='slug',
            field=models.CharField(max_length=500, null=True),
        ),
        migrations.AlterField(
            model_name='pac',
            name='slug',
            field=models.CharField(max_length=500, null=True),
        ),
    ]
