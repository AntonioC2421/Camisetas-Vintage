from VistaAdmin.models import Categorias, Teams, SubCategoria
from VistaAdmin.forms import *

#Estas variables se configuran en Settings para que sepuedan usar en cualquier template
def categorias_disponibles(request):
    categories = Categorias.objects.all()
    return {
        'category': categories,
    }

def admin_camisetas(request):
    teams = Teams.objects.all().order_by('-id')

    return {
        'datateams': teams,
    }

def formulario_addcamiseta(request):
    cam = ADDcamisetasForm()

    return {
        'FormADDcamiseta': cam,
    }

def codigos_disponibles(request):
    datecodprom = CodigoPromocional.objects.all()

    return{
        'datoscodigos': datecodprom
    }

def formulario_addcod(request):
    cam = FormCodPromo()

    return {
        'FormCodProm' : cam
    }

def subcategorias_disponibles(request):
    subCategoria = SubCategoria.objects.all()
    return {
        'subCaregoria':subCategoria
        }

def ItemsCardUser(request):
    context = {
        'users': None,
        'user_rut': None,
        'datosItems': []
    }

    if request.user.is_authenticated:
        try:
            cliente = Model_Client.objects.get(user=request.user)
            context['users'] = cliente.nombre
            context['user_rut'] = cliente.rut
            
            context['datosItems'] = Model_shopping_cart.objects.filter(id_cliente=cliente)
        except Model_Client.DoesNotExist:
            
            pass

    return context
