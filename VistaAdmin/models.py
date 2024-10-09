from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Size(models.Model):
    name = models.CharField(max_length=10)
    
class Categorias(models.Model):
    name = models.CharField(max_length=50)

class SubCategoria(models.Model):
    name = models.CharField(max_length=100)
    id_CategoriasCamisetas = models.ForeignKey(Categorias, on_delete=models.CASCADE)

class Marca(models.Model):
    name = models.CharField(max_length=100)

class CodigoPromocional(models.Model):
    name = models.CharField(max_length=100)
    descuento = models.IntegerField()
    vecesUso = models.IntegerField()

class Teams(models.Model):
    img= models.ImageField(upload_to='imgCamisetasVintage/', blank=True, null=True)
    name = models.CharField(max_length=100)
    year = models.IntegerField()
    precio = models.FloatField()
    id_SubCategoria = models.ForeignKey(SubCategoria,on_delete=models.CASCADE)
    id_Size = models.ForeignKey(Size,on_delete=models.CASCADE)
    id_Marca = models.ForeignKey(Marca,on_delete=models.CASCADE)
    
class TeamsImgs(models.Model):
    teams = models.ForeignKey(Teams, related_name='images', on_delete=models.CASCADE)
    imagen = models.ImageField(upload_to='imgCamisetasVintage/', blank=True, null=True)

class Model_Client(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='client_profile')
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    rut = models.CharField(max_length=9, unique=True)
    
class Model_shopping_cart(models.Model):
    fecha= models.DateTimeField()
    id_Teams = models.ForeignKey(Teams,on_delete=models.CASCADE)
    id_cliente = models.ForeignKey(Model_Client,on_delete=models.CASCADE)

class Model_Venta(models.Model):
    items_cart = models.ForeignKey(Teams, on_delete=models.CASCADE)
    rut_cliente = models.ForeignKey(Model_Client,on_delete=models.CASCADE)
    fecha_venta = models.DateTimeField()
    precio_venta = models.IntegerField()