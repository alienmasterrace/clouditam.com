# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-08-17 21:05
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0024_auto_20160817_2350'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dashuser',
            name='country',
            field=models.CharField(blank=True, choices=[('', 'Select Country'), ('Turkey', 'Turkey')], max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='dashuser',
            name='email',
            field=models.EmailField(max_length=254),
        ),
        migrations.AlterField(
            model_name='hardware',
            name='image',
            field=models.ImageField(blank=True, upload_to='suppliers'),
        ),
        migrations.AlterField(
            model_name='hardware',
            name='manufacturer',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='dashboard.Manufacturer'),
        ),
        migrations.AlterField(
            model_name='hardware',
            name='notes',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='location',
            name='country',
            field=models.CharField(choices=[('', 'Select Country'), ('Turkey', 'Turkey')], max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='supplier',
            name='country',
            field=models.CharField(choices=[('', 'Select Country'), ('Turkey', 'Turkey')], max_length=255, null=True),
        ),
    ]
