# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2017-01-18 12:28
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('rip_app', '0007_auto_20170118_1524'),
    ]

    operations = [
        migrations.AlterField(
            model_name='membersmodel',
            name='user',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='member', to=settings.AUTH_USER_MODEL),
        ),
    ]
