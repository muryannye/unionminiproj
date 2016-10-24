from django import forms
from .models import Computer

class SubmitComputer(forms.ModelForm):
    class Meta:
        model = Computer
        fields = ('serial_number', 'manufacturer','comments')
