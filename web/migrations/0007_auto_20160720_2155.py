# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-07-20 18:55
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0006_auto_20160720_2154'),
    ]

    operations = [
        migrations.AlterField(
            model_name='header',
            name='page',
            field=models.IntegerField(choices=[(1, 'Index'), (2, 'Pricing'), (3, 'Clients'), (4, 'Contact'), (5, 'About')], default=1, max_length=64),
        ),
    ]
