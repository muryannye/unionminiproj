from django import forms
from .models import Computer

class ComputerForm(forms.ModelForm):
    class Meta:
        model = Computer
        fields = ('serial_number', 'manufacturer','comments')
