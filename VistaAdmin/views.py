from django.shortcuts import render
from .models import Categorias
#Pagina Principal de el Admin
def MainPrincipal(request):
    return render(request, './TemplatesAdmin/Principal/Principal.html')