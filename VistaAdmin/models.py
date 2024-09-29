from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Size(models.Model):
    name = models.CharField(max_length=10)
    
    def __str__(self):
        return str(self.name) 
    
class Categorias(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return str(self.name) 
    
class SubCategoria(models.Model):
    name = models.CharField(max_length=100)
    id_CategoriasCamisetas = models.ForeignKey(Categorias, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.name) 

class Marca(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return str(self.name) 
    
class CodigoPromocional(models.Model):
    name = models.CharField(max_length=100)
    descuento = models.IntegerField()
    vecesUso = models.IntegerField()

    def __str__(self):
        return str(self.name) 

class Teams(models.Model):
    img= models.ImageField(upload_to='imgCamisetasVintage/', blank=True, null=True)
    name = models.CharField(max_length=100)
    year = models.IntegerField()
    precio = models.FloatField()
    id_SubCategoria = models.ForeignKey(SubCategoria,on_delete=models.CASCADE)
    id_Size = models.ForeignKey(Size,on_delete=models.CASCADE)
    id_Marca = models.ForeignKey(Marca,on_delete=models.CASCADE)

    def __str__(self):
        return str(self.name) 
    
class TeamsImgs(models.Model):
    teams = models.ForeignKey(Teams, related_name='images', on_delete=models.CASCADE)
    imagen = models.ImageField(upload_to='imgCamisetasVintage/', blank=True, null=True)

    def __str__(self):
        return f'Foto de camiseta: {self.teams}'

class Model_Client(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='client_profile')
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    rut = models.CharField(max_length=9, unique=True)
    def __str__(self):
        return str(self.rut)
    
class Model_shopping_cart(models.Model):
<<<<<<< HEAD
    fecha= models.DateTimeField()
=======
    fecha= models.DateTimeField('Fecha')
>>>>>>> ab94e0bb148cb187ec9f7249ad53c2663e161111
    id_Teams = models.ForeignKey(Teams,on_delete=models.CASCADE)
    id_cliente = models.ForeignKey(Model_Client,on_delete=models.CASCADE)

    def __str__(self):
<<<<<<< HEAD
        return f'{self.id_cliente} - {self.id_Teams}'
=======
        return str(self.id_Teams)
>>>>>>> ab94e0bb148cb187ec9f7249ad53c2663e161111
