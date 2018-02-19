# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-02-19 00:05
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('program', '0002_auto_20180219_0137'),
    ]

    operations = [
        migrations.AlterField(
            model_name='slot',
            name='track_span',
            field=models.IntegerField(choices=[(1, 'Single track'), (2, 'All tracks')], help_text='Does the slot span one track or all tracks (like keynote talks and breaks)'),
        ),
    ]
