# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2017-01-06 15:54
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('rip_app', '0016_auto_20170106_1606'),
    ]

    operations = [
        migrations.AddField(
            model_name='membersmodel',
            name='user',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='member', to=settings.AUTH_USER_MODEL),
        ),
    ]