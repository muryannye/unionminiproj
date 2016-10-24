# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import get_object_or_404, render, redirect
from .forms import ComputerForm, UpdateComputer
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

def computer(request, computer_id, folder_id):
    folder = get_object_or_404(Folder, pk=folder_id)
    computer = get_object_or_404(Computer, pk=computer_id)
    return render(request, 'inventory/computer.html', {'computer': computer}, {'folder': folder})

def add(request, folder_id):
    if request.method == "POST":
        form = ComputerForm(request.POST)
        if form.is_valid():
            obj = form.save(commit=False)
            obj.folder = Folder.objects.get(pk=folder_id)
            obj.save()
            url = "/inventory/" + str(folder_id) + "/"
            return HttpResponseRedirect(url)
    else:
        form = ComputerForm()
    return render(request, 'inventory/add.html', {'form': form})

def update(request, computer_id, folder_id):
   comp = get_object_or_404(Computer,pk=computer_id)
   if request.method == "POST":
       form = UpdateComputer(request.POST, instance=comp)
       if form.is_valid():
           form.save()
           url = "/inventory/" + str(folder_id) + "/" + str(computer_id) + "/"
           return HttpResponseRedirect(url)
   else:
        form = UpdateComputer()
   return render(request, 'inventory/update.html', {'form':form})

# def delete_computer(request, computer_id):
#    comp = get_object_or_404(Computr, pk=computer_id)
#    comp.delete()
#    return HttpResponse('deleted')
#

# def delete_folder(request, folder_id):
#     folder = get_object_or_404(Folder, pk=folder_id)
#     folder.delete()
#     return HttpResponse('deleted')
