# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-09-17 15:24
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('management', '0006_auto_20160917_1308'),
    ]

    operations = [
        migrations.AddField(
            model_name='gymmember',
            name='fees_structure',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='management.FeesStructure'),
        ),
    ]
