# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2017-01-03 11:13
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('rip_app', '0013_auto_20170103_1344'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='officesmodel',
            name='info',
        ),
    ]
