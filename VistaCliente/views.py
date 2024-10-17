from django.shortcuts import render
from VistaAdmin.models import *
from django.core.serializers import serialize
from django.db.models import Q
from VistaAdmin.models import *
from django.http import JsonResponse
from VistaAdmin.forms import *
import json

def MainPrincipalCliente(request):
    Equipo = Teams.objects.all().order_by('-id')[0:10]
    imgTeam = TeamsImgs.objects.all()
    imgTeam_serialized = serialize('json', imgTeam)
    data = {'equipos': Equipo, 'imgTeam': imgTeam_serialized}
    return render(request, './TemplatesClientes/MainCliente/IndexCliente.html', data)

def ViewItemsCart(request):
    items_cart = []
    
    if request.user.is_authenticated:
        if not request.user.is_staff:
            
            cliente = Model_Client.objects.get(user=request.user)
            
            items_cart = Model_shopping_cart.objects.filter(id_cliente=cliente)
            
            items = [{'id': item.id, 'name': item.id_Teams.name, 'id_teams': item.id_Teams.id} for item in items_cart]
            
            # Verifica si la solicitud es AJAX
            if request.headers.get('x-requested-with') == 'XMLHttpRequest':
                return JsonResponse({'success': True, 'message': 'Datos de Items', 'items': items})
    
    # Si no es una solicitud AJAX, renderiza el HTML con los datos
    data = {'datosItems': items_cart}
    return render(request, './TemplatesClientes/MainCliente/IndexCliente.html', data)

def Realizar_Venta(request):
    if request.method == 'POST':
        try:
            if request.user.is_authenticated:
                # Cargar los datos del cuerpo de la solicitud
                data = json.loads(request.body)
                precio_venta = data.get('precio_venta')
                items = data.get('items_cart')
                timestamp = data.get('timestamp')
                rut_cliente = data.get('rut_Cliente')

                print(f'Buscando cliente con RUT: {rut_cliente}')
                try:
                    user_id = Model_Client.objects.get(rut=rut_cliente)
                except Model_Client.DoesNotExist:
                    return JsonResponse({'success': False, 'message': 'Cliente no encontrado'})

                # Guardar cada ítem
                for item in items:
                    item_id = item.get('id_teams')
                    print(f'Buscando equipo con ID: {item_id}')

                    try:
                        equipo = Teams.objects.get(id=item_id)
                    except Teams.DoesNotExist:
                        return JsonResponse({'success': False, 'message': 'Equipo no encontrado'})

                    if not timestamp:
                        return JsonResponse({'success': False, 'message': 'Fecha de la venta no especificada'})

                    form_data = {
                        'items_cart': equipo,
                        'rut_cliente': user_id,
                        'fecha_venta': timestamp,
                        'precio_venta': precio_venta
                    }

                    form = FormAddVenta(data=form_data)
                    if not form.is_valid():
                        return JsonResponse({'success': False, 'message': 'Formulario no válido', 'errors': form.errors})

                    form.save()

                return JsonResponse({'success': True, 'message': 'Venta registrada correctamente'})

        except Exception as e:
            return JsonResponse({'success': False, 'message': f'Error: {str(e)}'})

    return JsonResponse({'success': False, 'message': 'Método no permitido'}, status=405)

def ValidacionCod(request, cod_pro):
    if request.method == 'POST':
        if cod_pro:
            try:
                validatorCod = CodigoPromocional.objects.get(name=cod_pro)
                
                # Verificar las veces de uso
                veces_uso = validatorCod.vecesUso
                descuento = validatorCod.descuento
                
                if veces_uso > 0:
                    response_data = {
                        'success': True,
                        'descuentoPorcentaje': descuento,   # Porcentaje de descuento
                        'vecesDescuento': veces_uso         # Veces que puede usarse
                    }
                    return JsonResponse(response_data)
                else:
                    # Código agotado
                    return JsonResponse({'success': False, 'message': 'Código Agotado :('})
            except CodigoPromocional.DoesNotExist:
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