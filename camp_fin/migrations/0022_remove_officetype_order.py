# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-08-30 15:39
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('camp_fin', '0021_remove_office_order'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='officetype',
            name='order',
        ),
    ]