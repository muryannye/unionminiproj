# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

class Computers(models.Model):
    manufacturer =  models.CharField(max_length=250)
    comments = models.CharField(max_length=300)
    serial_number = models.CharField(max_length=100)
