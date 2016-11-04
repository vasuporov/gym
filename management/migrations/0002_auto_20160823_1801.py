# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-08-23 18:01
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('management', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='feespaymenthistory',
            name='gym_member',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='management.GymMember'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='gymmember',
            name='leaving_date',
            field=models.DateTimeField(default=None, null=True),
        ),
    ]
