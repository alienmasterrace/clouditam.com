# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-08-17 15:53
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0013_auto_20160817_1829'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='asset',
            name='id',
        ),
        migrations.AddField(
            model_name='asset',
            name='is_os',
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name='asset',
            name='application',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='software', to='dashboard.Software'),
        ),
        migrations.AlterField(
            model_name='asset',
            name='company',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='dashboard.Company'),
        ),
        migrations.AlterField(
            model_name='asset',
            name='cpu_count',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='asset',
            name='cpu_speed',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=64, null=True),
        ),
        migrations.AlterField(
            model_name='asset',
            name='disk_size',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=64, null=True),
        ),
        migrations.AlterField(
            model_name='asset',
            name='disk_type',
            field=models.CharField(blank=True, choices=[('TB', 'TB'), ('GB', 'GB'), ('MB', 'MB')], max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='asset',
            name='ip_address',
            field=models.GenericIPAddressField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='asset',
            name='location',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='dashboard.Location'),
        ),
        migrations.AlterField(
            model_name='asset',
            name='memory_size',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=64, null=True),
        ),
        migrations.AlterField(
            model_name='asset',
            name='memory_type',
            field=models.CharField(blank=True, choices=[('TB', 'TB'), ('GB', 'GB'), ('MB', 'MB')], max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='asset',
            name='name',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='asset',
            name='notes',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='asset',
            name='order_number',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='asset',
            name='os',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='os', to='dashboard.Software'),
        ),
        migrations.AlterField(
            model_name='asset',
            name='platform',
            field=models.CharField(blank=True, choices=[('Physical', 'Physical')], max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='asset',
            name='purchase_cost',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=64, null=True),
        ),
        migrations.AlterField(
            model_name='asset',
            name='purchase_date',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='asset',
            name='role',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='asset',
            name='serial',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='asset',
            name='supplier',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='dashboard.Supplier'),
        ),
        migrations.AlterField(
            model_name='asset',
            name='warranty',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
