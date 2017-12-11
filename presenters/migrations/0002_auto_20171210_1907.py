# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-12-10 17:07
from __future__ import unicode_literals

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('presenters', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='presenter',
            name='bio',
            field=ckeditor.fields.RichTextField(blank=True, help_text='Short description about the presenter', null=True),
        ),
    ]