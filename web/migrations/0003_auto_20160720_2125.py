# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-07-20 18:25
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0002_auto_20160720_2116'),
    ]

    operations = [
        migrations.AlterField(
            model_name='header',
            name='bg_image',
            field=models.ImageField(default='headers/web/images/headers/index.jpg', upload_to='headers'),
        ),
    ]
