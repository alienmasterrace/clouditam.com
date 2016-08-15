# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-08-14 14:56
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0005_auto_20160812_0915'),
    ]

    operations = [
        migrations.AlterField(
            model_name='hardware',
            name='category',
            field=models.CharField(choices=[('Asset', 'Asset'), ('Access Point', 'Access Point'), ('Chassis', 'Chassis'), ('Computer', 'Computer'), ('Switch', 'Switch'), ('Router', 'Router'), ('Firewall', 'Firewall'), ('Printer', 'Printer'), ('Scanner', 'Scanner'), ('Projector', 'Projector'), ('Phone', 'Phone'), ('Tablet', 'Tablet'), ('Mobile Phone', 'Mobile Phone'), ('Video Conference', 'Video Conference'), ('VoIP Gateway', 'VoIP Gateway'), ('VoIP Phone', 'VoIP Phone'), ('Monitor', 'Monitor'), ('KVM (Keyboard, Video, Mouse switch)', 'KVM (Keyboard, Video, Mouse switch)'), ('Load Balancer', 'Load Balancer'), ('SAN (Storage Area Network)', 'SAN (Storage Area Network)'), ('NAS (Network Attached Storage', 'NAS (Network Attached Storage)'), ('Tape Library', 'Tape Library'), ('UPS', 'UPS'), ('General Purpose', 'General Purpose'), ('Other Computer Device', 'Other Computer Device'), ('Other Network Device', 'Other Network Device'), ('Other Security Device', 'Other Security Device'), ('Other Storage Device', 'Other Storage Device'), ('Other Telecom Device', 'Other Telecom Device'), ('Other Device', 'Other Device')], max_length=64, null=True),
        ),
        migrations.DeleteModel(
            name='Category',
        ),
    ]