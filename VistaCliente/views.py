from django.shortcuts import render
from VistaAdmin.models import Categorias, SubCategoria,Teams,Size,TeamsImgs,Marca,CodigoPromocional

def MainPrincipalCliente(request):
    Equipo = Teams.objects.all()
    data = {'equipos': Equipo}
    return render(request, './TemplatesClientes/MainCliente/IndexCliente.html',data)

def ViewCamisetas(request, id=None, team_id=None):
    SubCategory = SubCategoria.objects.filter(id_CategoriasCamisetas=id) #Real , Barcelona ... (Muestra los equipos de la Liga seleccionada)
    Equipo = Teams.objects.filter(id_SubCategoria__in=SubCategory) #Camiseta Real madrid 2018 (más img) | (Muetra las camisetas (img/info) del equipo seleccionado)

    if team_id:
        Equipo = Equipo.filter(id_SubCategoria=team_id) #Seleccionar una equipo y mostrar solo las camisetas de ese quipo

    encontrado = Equipo.exists() #si la liga tiene equipos dentro (true/false)

    data = {
        'equi': SubCategory,
        'camis': Equipo,
        'encontrado': encontrado,
        'idn': id,
        'selected_team_id': team_id,
    }
    return render(request, './TemplatesClientes/ViewCamisetas/ViewCamisetas.html', data)

def DetalleCamiseta(request, id):
    DetallesImG = TeamsImgs.objects.filter(teams = id)
    Detalle = Teams.objects.filter(id = id)
    data1 = {'imgs':DetallesImG}
    data3 = {"deta" : Detalle}
    data = {**data1,**data3}
    return render(request, './TemplatesClientes/DetalleCamiseta/DetalleCamiseta.html',data)