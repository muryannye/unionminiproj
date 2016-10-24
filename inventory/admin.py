# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

from .models import Folder, Computer

admin.site.register(Folder)
admin.site.register(Computer)
