from django.contrib import admin
from .models import Categorias,SubCategoria,Teams,Size,Marca,CodigoPromocional,TeamsImgs

# Register your models here.
admin.site.register(Categorias)
admin.site.register(SubCategoria)
admin.site.register(Teams)
admin.site.register(Size)
admin.site.register(Marca)
admin.site.register(CodigoPromocional)
admin.site.register(TeamsImgs)
