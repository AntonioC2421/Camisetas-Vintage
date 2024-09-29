from VistaAdmin.models import Categorias, Teams
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
