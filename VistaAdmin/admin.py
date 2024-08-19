from django.contrib import admin
from .models import Categorias,SubCategoria,Teams,Size

# Register your models here.
admin.site.register(Categorias)
admin.site.register(SubCategoria)
admin.site.register(Teams)
admin.site.register(Size)