from VistaAdmin.models import Categorias, Teams, SubCategoria
from VistaAdmin.forms import *
from django.core.serializers import serialize

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
    if request.user.is_authenticated:  # Verifica si el usuario está autenticado    
        cliente = Model_Client.objects.get(user=request.user)
        user_name = cliente.nombre
        user_rut = cliente.rut
        # Filtrar los items del carrito por el cliente logueado
        items_cart = Model_shopping_cart.objects.filter(id_cliente=cliente)

        return {
            'users': user_name,
            'datosItems': items_cart,
            'user_rut': user_rut
        }    