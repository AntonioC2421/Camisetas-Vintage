from django.shortcuts import render
from VistaAdmin.models import Categorias, SubCategoria,Teams,Size,TeamsImgs,Marca,CodigoPromocional
from django.core.serializers import serialize
from django.db.models import Q #Consultas para la barra de busqueda

def MainPrincipalCliente(request):
    Equipo = Teams.objects.all().order_by('-id')[0:8]
    imgTeam = TeamsImgs.objects.all()
    imgTeam_serialized = serialize('json', imgTeam)
    
    data = {'equipos': Equipo,'imgTeam': imgTeam_serialized}
    
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
    data = {'imgs':DetallesImG, "deta" : Detalle}
    return render(request, './TemplatesClientes/DetalleCamiseta/DetalleCamiseta.html',data)

def Search(request):
    query = request.GET.get('q')  # Obtiene la consulta de búsqueda
    teambus = None
    
    if query:  # Si hay una consulta, se ejecuta la búsqueda
        # Busca subcategorías cuyos nombres coincidan parcialmente con la consulta
        subcategorias = SubCategoria.objects.filter(name__icontains=query)
        
        # Filtra los equipos basados en:
        # 1. El nombre del equipo que coincida con la búsqueda
        # 2. Los equipos que pertenezcan a subcategorías que coincidan con la búsqueda
        teambus = Teams.objects.filter(
            Q(name__icontains=query) |  # Busca por nombre de equipo
            Q(id_SubCategoria__in=subcategorias)  # Busca por subcategoría relacionada
        )

    return render(request, 'TemplatesClientes/MainCliente/Busquedas.html', {'teams': teambus, 'query': query})