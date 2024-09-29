from django.shortcuts import render
<<<<<<< HEAD
from VistaAdmin.models import SubCategoria,Teams,TeamsImgs
from django.core.serializers import serialize
from django.db.models import Q #Consultas para la barra de busqueda
from VistaAdmin.models import *
from django.http import JsonResponse
=======
from VistaAdmin.models import Categorias, SubCategoria,Teams,Size,TeamsImgs,Marca,CodigoPromocional
from django.core.serializers import serialize
from django.db.models import Q #Consultas para la barra de busqueda

>>>>>>> ab94e0bb148cb187ec9f7249ad53c2663e161111
def MainPrincipalCliente(request):
    Equipo = Teams.objects.all().order_by('-id')[0:8]
    imgTeam = TeamsImgs.objects.all()
    imgTeam_serialized = serialize('json', imgTeam)
    
<<<<<<< HEAD
    if request.user.is_authenticated:  # Verifica si el usuario está autenticado
        if request.user.is_staff:
            items_cart = []
            data = {'equipos': Equipo, 'imgTeam': imgTeam_serialized}
        else:
            # Obtén el cliente relacionado con el usuario logueado
            cliente = Model_Client.objects.get(user=request.user)
            user_name = cliente.nombre
            # Filtra los items del carrito por el cliente logueado
            items_cart = Model_shopping_cart.objects.filter(id_cliente=cliente)
            data = {'users': user_name ,'equipos': Equipo, 'imgTeam': imgTeam_serialized, 'datosItems': items_cart}
    else:
        data = {'equipos': Equipo, 'imgTeam': imgTeam_serialized}

    return render(request, './TemplatesClientes/MainCliente/IndexCliente.html', data)

def ViewItemsCart(request):
    if request.user.is_authenticated:  # Verifica si el usuario está autenticado
        if request.user.is_staff:
            items_cart = []
        else:
            # Obtén el cliente relacionado con el usuario logueado
            cliente = Model_Client.objects.get(user=request.user)
            user_name = cliente.nombre
            # Filtra los items del carrito por el cliente logueado
            items_cart = Model_shopping_cart.objects.filter(id_cliente=cliente)
            
    data = {'datosItems': items_cart,'users':user_name}

    return render(request, './TemplatesClientes/MainCliente/IndexCliente.html', data)


def DeleteItemsCart(request, id_item):
    if request.method == 'POST':
        try:
            idItemsCartDelete = Model_shopping_cart.objects.get(id=id_item)
            print(f"El valor de id_item es: {id_item}")
            idItemsCartDelete.delete()
            return JsonResponse({'success': True, 'message': 'Item eliminado correctamente'})
        except Model_shopping_cart.DoesNotExist:
            return JsonResponse({'success':False, 'message': 'Item no encontrado'})
    return JsonResponse({'success': False, 'message': 'Método no permitido'}, status=405)
=======
    data = {'equipos': Equipo,'imgTeam': imgTeam_serialized}
    
    return render(request, './TemplatesClientes/MainCliente/IndexCliente.html',data)
>>>>>>> ab94e0bb148cb187ec9f7249ad53c2663e161111

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
    
<<<<<<< HEAD
    if query:
=======
    if query:  # Si hay una consulta, se ejecuta la búsqueda
>>>>>>> ab94e0bb148cb187ec9f7249ad53c2663e161111
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