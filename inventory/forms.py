from django import forms
from .models import Computer, Folder
from django.views.generic.edit import DeleteView

class ComputerForm(forms.ModelForm):
    class Meta:
        model = Computer
        fields = ('serial_number', 'manufacturer','comments',)

class FolderForm(forms.ModelForm):
    class Meta:
        model = Folder
        fields = ('folder_name',)

class EditComputer(forms.ModelForm):
    comments = forms.CharField(required=False)
    class Meta:
        model = Computer
        fields = ('folder', 'serial_number', 'manufacturer','comments',)
