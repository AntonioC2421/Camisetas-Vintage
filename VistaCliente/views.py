from django.shortcuts import render
from VistaAdmin.models import Categorias, SubCategoria,Teams,Size

def MainPrincipalCliente(request):
    Category = Categorias.objects.all()
    Equipo = Teams.objects.all()
    data = {'category': Category, 'equipos': Equipo}
    return render(request, './TemplatesClientes/MainCliente/IndexCliente.html',data)

def ViewCamisetas(request, id=None, team_id=None):
    Category = Categorias.objects.all()
    SubCategory = SubCategoria.objects.filter(id_CategoriasCamisetas=id)
    Equipo = Teams.objects.filter(id_SubCategoria__in=SubCategory)

    if team_id:
        Equipo = Equipo.filter(id=team_id)

    encontrado = False
    for cam in Equipo:
        if cam.id_SubCategoria.id_CategoriasCamisetas.id == id:
            encontrado = True
            break

    data = {
        'equi': SubCategory,
        'category': Category,
        'camis': Equipo,
        'encontrado': encontrado,
        'idn': id,
    }
    return render(request, './TemplatesClientes/ViewCamisetas/ViewCamisetas.html', data)
