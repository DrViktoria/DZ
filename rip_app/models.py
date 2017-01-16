# Create your models here.
# -*- coding: utf-8 -*-

from __future__ import unicode_literals
from django.db import models
from django.contrib.auth.models import User


class OfficesModel(models.Model):
    named = models.CharField(max_length=30, verbose_name=u'Название')
    location = models.CharField(max_length=255, verbose_name=u'Адрес')
    picture = models.ImageField(upload_to="images/", null=True, verbose_name=u'')

    def __str__(self):
        return self.named


class MembersModel(models.Model):
    office = models.ManyToManyField(OfficesModel, related_name="members")
    name = models.CharField(max_length=100, verbose_name=u'Name')
    position = models.CharField(max_length=255, verbose_name=u'Position')
    photo = models.ImageField(upload_to="images/", null=True)
    username = models.CharField(max_length=255, null=False, default='login')
    password = models.CharField(max_length=255, null=False, default='12345')
    user = models.OneToOneField(User, null=True, related_name='member')

    def __str__(self):
        return self.name






