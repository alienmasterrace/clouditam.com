# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-08-14 16:56
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0006_auto_20160814_1756'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Application',
            new_name='Software',
        ),
    ]