from .models import *
from django import forms

class ADDcamisetasForm(forms.ModelForm):
    class Meta:
        model = Teams
        fields = ('img','name','year','precio','id_Marca','id_Size','id_SubCategoria')