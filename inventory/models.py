# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.utils.encoding import python_2_unicode_compatible

@python_2_unicode_compatible
class Folder(models.Model):
    folder_name = models.CharField(max_length=200)
    def __str__(self):
        return self.folder_name

@python_2_unicode_compatible
class Computer(models.Model):
    folder = models.ForeignKey(Folder, on_delete=models.CASCADE, null=True)
    serial_number = models.CharField(max_length=100)
    manufacturer =  models.CharField(max_length=250)
    comments = models.TextField(max_length=300, default="")
    def __str__(self):
        return self.serial_number
