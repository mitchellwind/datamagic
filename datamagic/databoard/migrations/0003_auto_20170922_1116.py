# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-09-22 03:16
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('databoard', '0002_auto_20170922_1052'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mydata',
            name='end_time',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='mydata',
            name='start_time',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
