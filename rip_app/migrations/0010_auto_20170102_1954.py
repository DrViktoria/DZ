# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2017-01-02 16:54
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('rip_app', '0009_officesmodel_info'),
    ]

    operations = [
        migrations.AddField(
            model_name='officesmodel',
            name='picture',
            field=models.FileField(null=True, upload_to='static/images'),
        ),
        migrations.AlterField(
            model_name='membersmodel',
            name='office',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='members', to='rip_app.OfficesModel'),
        ),
    ]