# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-07-20 18:30
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0003_auto_20160720_2125'),
    ]

    operations = [
        migrations.AlterField(
            model_name='header',
            name='bg_image',
            field=models.ImageField(default='headers/default.jpg', upload_to='headers'),
        ),
    ]
