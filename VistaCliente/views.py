from django.shortcuts import render
from VistaAdmin.models import Categorias, SubCategoria,Teams,Size

def MainPrincipalCliente(request):
    Category = Categorias.objects.all()
    Equipo = Teams.objects.all()
    data = {'category': Category, 'equipos': Equipo}
    return render(request, './TemplatesClientes/MainCliente/IndexCliente.html',data)

def ViewCamisetas(request,id):
    Category = Categorias.objects.all()
    SubCategory = SubCategoria.objects.filter(id_CategoriasCamisetas = id)
    Equipo = Teams.objects.all()
    data = {'equi': SubCategory,'category': Category, 'camis': Equipo}
    return render(request, './TemplatesClientes/ViewCamisetas/ViewCamisetas.html', data)