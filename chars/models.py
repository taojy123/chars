# -*- coding: utf-8 -*-

from django.db import models
class Char(models.Model):
    level = models.IntegerField()
    chars = models.CharField(max_length=2048, blank=True , null=True)
