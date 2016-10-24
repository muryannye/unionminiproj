# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import get_object_or_404, render, redirect
from .forms import ComputerForm
from django.template import loader
from django.http import HttpResponse, HttpResponseRedirect
from .models import Folder, Computer

def index(request):
    all_folders = Folder.objects.all()
    template = loader.get_template('inventory/index.html')
    context = {
        'all_folders': all_folders,
    }
    return HttpResponse(template.render(context, request))

def detail(request, folder_id):
    folder = get_object_or_404(Folder, pk=folder_id)
    return render(request, 'inventory/detail.html', {'folder': folder})

def add(request, folder_id):
    if request.method == "POST":
        form = ComputerForm(request.POST)
        if form.is_valid():
            obj = form.save(commit=False)
            obj.folder = Folder.objects.get(pk=folder_id)
            obj.save()
            return HttpResponseRedirect('/inventory/(?P<folder_id>[0-9]+)/$')
    else:
        form = ComputerForm()
    return render(request, 'inventory/add.html', {'form': form})
