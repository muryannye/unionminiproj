# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse
from .models import Folder

def index(request):
    all_folders = Folder.objects.all()
    template = loader.get_template('inventory/index.html')
    context = {
        'all_folders': all_folders,
    }
    return HttpResponse(template.render(context, request))

def detail(request, folder_id):
    try:
        folder = Folder.objects.get(pk=folder_id)
    except Folder.DoesNotExist:
        raise Http404("Folder does not exist")
    return render(request, 'inventory/detail.html', {'folder': folder})
