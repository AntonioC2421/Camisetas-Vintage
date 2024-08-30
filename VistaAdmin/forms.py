from .models import *
from django import forms

class ADDcamisetasForm(forms.ModelForm):
    class Meta:
        model = Teams
        fields = '__all__'