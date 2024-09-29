from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout,login,authenticate
from django.shortcuts import redirect
from .forms import *
from .models import *
from django.views import View
from django.http import JsonResponse


# Decorador para verificar si el usuario es admin
def admin_required(view_func):
    def _wrapped_view(request, *args, **kwargs):
        if request.user.is_authenticated and request.user.is_staff:
            return view_func(request, *args, **kwargs)
        else:
            # Redirige a la vista deseada sin el parámetro next
            return redirect('ViewsClient:MainPrincipalCliente')  # Cambia esto a la vista que desees
    return _wrapped_view

@login_required
def redirigir_usuario(request): #redirigir según usuario
    
        if request.user.is_staff and request.user.is_active:
            return redirect('ViewsAdmin:PrincipalAdmin')  # Vista del administrador
        elif not request.user.is_staff and request.user.is_active:
            return redirect('ViewsClient:MainPrincipalCliente')  # Vista para el cliente

def is_admin(user): #Verificar si es Admin o Cliente
    return user.is_staff

#Pagina Principal de el Admin
@login_required
@admin_required  # Usa el decorador aquí
def MainPrincipal(request):
    return render(request, './TemplatesAdmin/Principal/Principal.html')

#Sección ADDMINISTRACIÓN DE CAMISETAS
@login_required
@admin_required 
def ADDcamisetas(request):
    cam = ADDcamisetasForm()

    if request.method == 'POST':
        if 'submit_cam' in request.POST:
            cam = ADDcamisetasForm(request.POST, request.FILES)
            if cam.is_valid():
                cam.save()
                return redirect('ViewsAdmin:ADDcamisetas')
            else:
                data['mensaje'] = 'Ocurrió un problema en el registro :"( !!'
    data = {'FormADDcamiseta': cam}

    return render(request, './TemplatesAdmin/ADDcamisetas/ADDcamisetas.html', data)

<<<<<<< HEAD
from django.http import JsonResponse
from django.utils import timezone
@login_required
def AddItemCart(request):
    if request.method == 'POST':
        # Capturamos manualmente los valores desde request.POST
        user_id = request.POST.get('user_id')
        item_id = request.POST.get('item_id')
        timestamp = request.POST.get('timestamp')

        # Verifica que los datos no sean nulos
        if user_id and item_id and timestamp:
            # Convertir a int y manejar excepciones
            try:
                user_id = int(user_id)
                item_id = int(item_id)
                timestamp = timezone.datetime.fromisoformat(timestamp)  # Convertir a DateTime
            except (ValueError, TypeError):
                return JsonResponse({'success': False, 'message': 'Datos de ID inválidos'})

            # Verificar existencia de cliente y equipo
            try:
                client = Model_Client.objects.get(user__id=user_id)
                team = Teams.objects.get(id=item_id)
            except Model_Client.DoesNotExist:
                return JsonResponse({'success': False, 'message': 'El cliente no existe'})
            except Teams.DoesNotExist:
                return JsonResponse({'success': False, 'message': 'El equipo no existe'})

            # Crear el formulario con los datos
            form_data = {
                'id_cliente': client.id,  # Usar el ID del cliente
                'id_Teams': team.id,      # Usar el ID del equipo
                'fecha': timestamp         # Asignar la fecha
            }
            form = FormAddItemCart(data=form_data)  # Crear formulario con datos

            # Verifica si el formulario es válido
            if form.is_valid():
                form.save()  # Guardar el objeto en la base de datos
                return JsonResponse({'success': True, 'message': 'Item agregado correctamente'})
            else:
                print("Errores del formulario:", form.errors)  # Imprimir errores de validación
                return JsonResponse({'success': False, 'message': 'Datos no válidos', 'errors': form.errors})
        else:
            return JsonResponse({'success': False, 'message': 'Faltan datos requeridos'})

=======
>>>>>>> ab94e0bb148cb187ec9f7249ad53c2663e161111
def ADDimgCamiseta(request, id):
    team = Teams.objects.get(id=id)
    addimgform = ADDimgCamisetas()
    imgsTeam = TeamsImgs.objects.filter(teams=id).order_by('-id')
    if request.method == 'POST':
        if 'submit_img' in request.POST:
            addimgform = ADDimgCamisetas(request.POST, request.FILES)
            if addimgform.is_valid():
                addimgform_instance = addimgform.save(commit = False)
                addimgform_instance.teams = team
                addimgform_instance.save()
                return redirect ('ViewsAdmin:ADDimgcamisetas', id = id)
    data = {
        'FormAddImg' : addimgform,
        'imgs':imgsTeam,
    }
    
    return render(request, './TemplatesAdmin/ADDcamisetas/ADDimgCamisetas.html',data)


def DeleteImg(request, img_id):
    img = TeamsImgs.objects.get(id=img_id)
    team_id= request.POST['img_id']
    img.delete()
    return redirect ('ViewsAdmin:ADDimgcamisetas', id = team_id)

def ChangeInfoCamiseta(request,id_team):
    team = Teams.objects.get(id = id_team)
    data = {'ChangeInfo' : ADDcamisetasForm(instance=team)}
    if request.method == 'POST':
        form = ADDcamisetasForm(data=request.POST, instance=team)
        if form.is_valid():
            form.save()
            return redirect('ViewsAdmin:ADDcamisetas')
        data['ChangeInfo'] = form

    return render(request, './TemplatesAdmin/ADDcamisetas/ChangeCamisetas.html', data)

def DeleteTeam(request, id_team):
    team = Teams.objects.get(id = id_team)
    if request.method == 'POST':
        team.delete()
        return redirect('ViewsAdmin:ADDcamisetas')
    return render(request,'./TemplatesAdmin/ADDcamisetas/DeleteCamisetas.html', {'id_team': id_team})

#Sección CODIGOS PROMOCIONALES
@login_required
@admin_required 
def CodiPromoViews(request):
    forcodi = FormCodPromo()
    data = {'FormCodProm' : forcodi}
    if request.method == 'POST':
        forcodi = FormCodPromo(request.POST)
        if forcodi.is_valid():
            forcodi.save()
            return redirect('ViewsAdmin:CodPromUrl')
    
    return render(request, './TemplatesAdmin/CodigosPromocionales/CodPromo.html',data)

def ChangeInfoCod(request, id_cod):
    cod = CodigoPromocional.objects.get(id = id_cod)
    data = {'ChangeInfo' : FormCodPromo(instance=cod)}
    if request.method == 'POST':
        form = FormCodPromo(data= request.POST, instance=cod)
        if form.is_valid():
            form.save()
            return redirect('ViewsAdmin:CodPromUrl')
        data['ChangeInfo'] = form
    return render(request,'./TemplatesAdmin/CodigosPromocionales/CodPromoChange.html',data)

def DeleteCodPromo(request, id_cod):
    cod = CodigoPromocional.objects.get(id = id_cod)
    if request.method == 'POST':
        cod.delete()
        return redirect('ViewsAdmin:CodPromUrl')
    return render(request, './TemplatesAdmin/CodigosPromocionales/CodPromoDelete.html')

#sección AGREGAR: Marcas, Ligas, Equipo
class ViewDatos(View):
    
    def eliminar_datos(request, id_dato):
        if request.method == 'POST':
            # Obtener el valor del tipo de dato enviado desde el POST
            tipo_dato = request.POST.get('id-dato-delete')
            if tipo_dato == 'marca':
                try:
                    marca = Marca.objects.get(id=id_dato)
                    marca.delete()
                    return JsonResponse({'success': True, 'message': 'Marca eliminada correctamente'})
                except Marca.DoesNotExist:
                    return JsonResponse({'success': False, 'message': 'Marca no encontrada'})
            elif tipo_dato == 'liga':
                try:
                    liga = Categorias.objects.get(id=id_dato)
                    liga.delete()
                    return JsonResponse({'success': True, 'message': 'Liga eliminada correctamente'})
                except Categorias.DoesNotExist:
                    return JsonResponse({'success': False, 'message': 'Liga no encontrada'})
            elif tipo_dato == 'equipo':
                try:
                    equipo = SubCategoria.objects.get(id=id_dato)
                    equipo.delete()
                    return JsonResponse({'success': True, 'message': 'Equipo eliminado correctamente'})
                except SubCategoria.DoesNotExist:
                    return JsonResponse({'success': False, 'message': 'Equipo no encontrada'})
            elif tipo_dato == 'talla':
                try:
                    talla = Size.objects.get(id = id_dato)
                    talla.delete()
                    return JsonResponse({'success': True, 'message': 'Talla eliminado correctamente'})
<<<<<<< HEAD
                except Size.DoesNotExist:
=======
                except SubCategoria.DoesNotExist:
>>>>>>> ab94e0bb148cb187ec9f7249ad53c2663e161111
                    return JsonResponse({'success': False, 'message': 'Talla no encontrada'})
        return JsonResponse({'success': False, 'message': 'Método no permitido'}, status=405)
    @login_required
    @admin_required 
    def viewsAgregarDatos(request):
            if request.method == 'POST':
                if 'submit-marca' in request.POST:
                    form = FormsAddMarcas(request.POST)
                    if form.is_valid():
                        nueva_marca = form.save()
                        response_data = {
                            'success': True,
                            'new_marca': {
                                'id': nueva_marca.id,
                                'name': nueva_marca.name
                            }
                        }
                        return JsonResponse(response_data)
                    else:
                        return JsonResponse({'success': False, 'errors': form.errors})
                    
                elif 'submit-liga' in request.POST:
                    formLiga = FormAddCategorias(request.POST)
                    if formLiga.is_valid():
                        nueva_liga = formLiga.save()
                        response_data = {
                            'success' : True,
                            'new_liga' : {
                                'id': nueva_liga.id,
                                'name':nueva_liga.name
                            }
                        }
                        return JsonResponse(response_data)
                    else:
                        return JsonResponse({'success': False, 'errors':formLiga.errors})
                elif 'submit-equipos' in request.POST:
                    formEquipos = FormsAddSubcategorias(request.POST)
                    if formEquipos.is_valid():
                        nuevo_Equipo = formEquipos.save()
                        response_data = {
                            'success' : True,
                            'new_equipo' : {
                                'id': nuevo_Equipo.id,
                                'name' : nuevo_Equipo.name,
                                'id_CategoriasCamisetas': nuevo_Equipo.id_CategoriasCamisetas.id,
                                'categoria_name': nuevo_Equipo. id_CategoriasCamisetas.name, #Pasar el nombre de Liga para renderizar
                            }
                        }
                        return JsonResponse(response_data)
                    else:
                        return JsonResponse({'success': False, 'errors':formEquipos.errors})
                elif 'submit-tallas' in request.POST:
                    formTallas = FormsAddSize(request.POST)
                    if formTallas.is_valid():
                        nueva_talla = formTallas.save()
                        response_data = {
                            'success': True,
                            'new_talla': {
                                'id' : nueva_talla.id,
                                'name': nueva_talla.name,
                            }
                        }
                        return JsonResponse(response_data)
                    else:
                        return JsonResponse({
                            'success': False,
                            'errors':formTallas.errors
                        })
                    
            marcas = Marca.objects.all()
            ligas = Categorias.objects.all()
            equipos = SubCategoria.objects.all()
            tallas = Size.objects.all()
            formTalla = FormsAddSize()
            formEquipos = FormsAddSubcategorias()
            formLigas = FormAddCategorias()
            form = FormsAddMarcas()
            data = {
                'FormsAddMarca': form,
                'marcas': marcas,
                'ligas': ligas,
                'FormAddLigas':formLigas,
                'FormAddEquipos' : formEquipos,
                'equipos':equipos,
                'FormAddTallas': formTalla,
                'tallas':tallas,
            }
            return render(request, './TemplatesAdmin/ADDdatos/MainAddDatos.html', data)

def ViewsAddCliente(request):
    form = FormsAddCliente()
    if request.method == 'POST':
        form = FormsAddCliente(request.POST)
        if form.is_valid():
            # Guardar el nuevo cliente
            client = form.save()

            # Autenticar al usuario recién creado
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request, username=username, password=password)

            if user is not None:
                login(request, user) # Iniciar sesión automáticamente
                return redirect('ViewsClient:MainPrincipalCliente')#Redirigir a la vista de cliente

    data = {'formAddCliente': form}
    return render(request, './authentication/CreateUser.html', data)

#Deslogueo
def exit(request):
    logout(request)
    return redirect('/Home/')