from django import forms
from .models import Computer
from django.views.generic.edit import DeleteView

class ComputerForm(forms.ModelForm):
    class Meta:
        model = Computer
        fields = ('serial_number', 'manufacturer','comments')

class UpdateComputer(forms.ModelForm):
    comments = forms.CharField(required=False)
    class Meta:
        model = Computer
        fields = ('folder', 'serial_number', 'manufacturer','comments')
