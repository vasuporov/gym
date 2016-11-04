# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-09-17 13:03
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('management', '0004_auto_20160917_1225'),
    ]

    operations = [
        migrations.AddField(
            model_name='gymmember',
            name='biceps_left',
            field=models.IntegerField(blank=True, default=None),
        ),
        migrations.AddField(
            model_name='gymmember',
            name='biceps_right',
            field=models.IntegerField(blank=True, default=None),
        ),
        migrations.AddField(
            model_name='gymmember',
            name='height',
            field=models.DecimalField(blank=True, decimal_places=2, default=None, max_digits=4),
        ),
        migrations.AddField(
            model_name='gymmember',
            name='triceps_left',
            field=models.IntegerField(blank=True, default=None),
        ),
        migrations.AddField(
            model_name='gymmember',
            name='triceps_right',
            field=models.IntegerField(blank=True, default=None),
        ),
        migrations.AddField(
            model_name='gymmember',
            name='weight',
            field=models.IntegerField(blank=True, default=None),
        ),
    ]
