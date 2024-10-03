from django.shortcuts import render
from VistaAdmin.models import SubCategoria,Teams,TeamsImgs
from django.core.serializers import serialize
from django.db.models import Q #Consultas para la barra de busqueda
from VistaAdmin.models import *
from django.http import JsonResponse

def MainPrincipalCliente(request):
    Equipo = Teams.objects.all().order_by('-id')[0:8]
    imgTeam = TeamsImgs.objects.all()
    imgTeam_serialized = serialize('json', imgTeam)
    
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


def ValidacionCod(request, cod_pro):
    if request.method == 'POST':
        if cod_pro:
            try:
                # Buscar el código promocional
                validatorCod = CodigoPromocional.objects.get(name=cod_pro)
                
                # Verificar las veces de uso
                veces_uso = validatorCod.vecesUso
                descuento = validatorCod.descuento
                
                if veces_uso > 0:
                    # Retornar el descuento si el código es válido
                    return JsonResponse({'success': True, 'message': 'Código canjeado', 'descuentoPorcentaje': descuento})
                else:
                    # Código agotado
                    return JsonResponse({'success': False, 'message': 'Código Agotado :('})
            except CodigoPromocional.DoesNotExist:
                # Si el código promocional no existe
                return JsonResponse({'success': False, 'message': 'Código no válido'})
        else:
            # Si no se proporcionó código
            return JsonResponse({'success': False, 'message': 'No se ingresó código promocional'})
    
    # Si no es una solicitud POST
    return render(request, './TemplatesClientes/MainCliente/IndexCliente.html')


def DeleteItemsCart(request, id_item):
    if request.method == 'POST':
        try:
            idItemsCartDelete = Model_shopping_cart.objects.get(id=id_item)
            
            idItemsCartDelete.delete()
            return JsonResponse({'success': True, 'message': 'Item eliminado correctamente'})
        except Model_shopping_cart.DoesNotExist:
            return JsonResponse({'success':False, 'message': 'Item no encontrado'})
    return JsonResponse({'success': False, 'message': 'Método no permitido'}, status=405)

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
    
    if query:
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