from .models import *
from django import forms
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError

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

class FormsAddCliente(forms.ModelForm):
    # Campos adicionales para el registro del usuario
    username = forms.EmailField( #Hice cambio en vez de nombre de usuario, un correo
        label="Correo Electrónico:",
        required=True,  # Para que sea obligatorio
        widget=forms.EmailInput(attrs={'placeholder': 'example@gmail.com'})  # Placeholder opcional
    )
    password = forms.CharField(
        widget=forms.PasswordInput,
        label="Contraseña:",
        help_text='Requerido. Ingrese una contraseña segura.'
    )
    
    class Meta:
        model = Model_Client
        fields = ['nombre','apellido', 'rut']  # Los campos del cliente

    # Sobrescribir el método save para crear tanto el usuario como el cliente
    def save(self, commit=True):
        # Crear el usuario primero
        user = User.objects.create_user(
            username=self.cleaned_data['username'],
            password=self.cleaned_data['password']
        )
        
        # Luego crear el cliente asociado al usuario
        client = super(FormsAddCliente, self).save(commit=False)
        client.user = user  # Asignar el usuario al cliente

        if commit:
            client.save()
        
        return client

    # Validación para asegurarse de que el correo electrónico sea único
    def clean_username(self):
        username = self.cleaned_data.get('username')
        if User.objects.filter(username=username).exists():
            raise ValidationError("Este correo electrónico ya está en uso.")
        return username
    
class FormAddItemCart(forms.ModelForm):
    class Meta:
        model = Model_shopping_cart
        fields = ['id_Teams', 'id_cliente', 'fecha']

    def clean_fecha(self):
        fecha = self.cleaned_data.get('fecha')
        if not fecha:
            raise forms.ValidationError("La fecha es un campo obligatorio.")
        return fecha