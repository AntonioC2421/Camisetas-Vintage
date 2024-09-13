from .models import *
from django import forms

class ADDcamisetasForm(forms.ModelForm):
    class Meta:
        model = Teams
        fields = ('img','name','year','precio','id_Marca','id_Size','id_SubCategoria')

class ADDimgCamisetas(forms.ModelForm):
    class Meta:
        model = TeamsImgs
        fields = {'imagen'}

class ChangeCamisetas(forms.ModelForm):
    class Meta:
        model = Teams
        fields = '__all__'

class FormCodPromo(forms.ModelForm):
    class Meta:
        model = CodigoPromocional
        fields = '__all__'

class FormAddCategorias(forms.ModelForm):
    class Meta:
        model = Categorias
        fields = '__all__'

class FormsAddSubcategorias(forms.ModelForm):
    class Meta:
        model = SubCategoria
        fields = '__all__'

class FormsAddSize(forms.ModelForm):
    class Meta:
        model = Size
        fields = '__all__'

class FormsAddMarcas(forms.ModelForm):
    class Meta:
        model = Marca
        fields = '__all__'