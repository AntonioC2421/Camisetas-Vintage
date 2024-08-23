from VistaAdmin.models import Categorias

def categorias_disponibles(request):
    categories = Categorias.objects.all()
    return {'category': categories}