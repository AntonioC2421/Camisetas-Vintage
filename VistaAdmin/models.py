from django.db import models

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

class CodigoPromocional(models.Model):
    name = models.CharField(max_length=100)
    descuento = models.IntegerField()
    vecesUso = models.IntegerField()

class Teams(models.Model):
    img = models.ImageField(upload_to='imgCamisetasVintage', blank=True, null=True)
    name = models.CharField(max_length=100)
    year = models.IntegerField()
    precio = models.FloatField()
    id_SubCategoria = models.ForeignKey(SubCategoria,on_delete=models.CASCADE)
    id_Size = models.ForeignKey(Size,on_delete=models.CASCADE)
    #id_Marca = models.ForeignKey(Marca,on_delete=models.CASCADE)

    def __str__(self):
        return str(self.name) 