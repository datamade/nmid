# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-09-23 13:56
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('camp_fin', '0049_auto_20160915_1347'),
    ]

    operations = [
        migrations.AlterField(
            model_name='candidate',
            name='full_name',
            field=models.CharField(max_length=500, null=True),
        ),
    ]
