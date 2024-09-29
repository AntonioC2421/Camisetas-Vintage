from django.contrib import admin
from .models import Categorias,SubCategoria,Teams,Size,Marca,CodigoPromocional,TeamsImgs,Model_Client,Model_shopping_cart

# Register your models here.
admin.site.register(Categorias)
admin.site.register(SubCategoria)
admin.site.register(Teams)
admin.site.register(Size)
admin.site.register(Marca)
admin.site.register(CodigoPromocional)
admin.site.register(TeamsImgs)
admin.site.register(Model_Client)
admin.site.register(Model_shopping_cart)
