# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-01-17 18:17
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('proposals', '0004_auto_20180117_2000'),
    ]

    operations = [
        migrations.AlterField(
            model_name='proposal',
            name='user',
            field=models.ForeignKey(blank=True, help_text='Issuer of the proposal', null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL),
        ),
    ]