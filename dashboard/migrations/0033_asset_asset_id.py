# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-08-18 04:15
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0032_auto_20160818_0702'),
    ]

    operations = [
        migrations.AddField(
            model_name='asset',
            name='asset_id',
            field=models.IntegerField(default=10000),
        ),
    ]
