# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-12-28 20:25
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rip_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='OfficesModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('named', models.CharField(max_length=30, verbose_name='Named')),
                ('location', models.TextField(max_length=255, verbose_name='Location')),
            ],
        ),
    ]
