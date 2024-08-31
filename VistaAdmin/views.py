from django.shortcuts import render
from .models import Categorias, SubCategoria,Teams,Size,TeamsImgs,Marca,CodigoPromocional
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from django.shortcuts import redirect
from .forms import *

#Pagina Principal de el Admin
@login_required
def MainPrincipal(request):
    return render(request, './TemplatesAdmin/Principal/Principal.html')

def ADDcamisetas(request):
    cam = ADDcamisetasForm()
    teams = Teams.objects.all()
    data = {'FormADDcamiseta' : ADDcamisetasForm(), 'datateams': teams}
    if request.method == 'POST':
        cam = ADDcamisetasForm(request.POST,request.FILES)
        if cam.is_valid():
            cam.save()
            return redirect('ViewsAdmin:ADDcamisetas')
        else:
            data['mensaje'] = 'Ocurrió un problema en el registro :"( !!'
    return render(request, './TemplatesAdmin/ADDcamisetas/ADDcamisetas.html',data)

def exit(request):
    logout(request)
    return redirect('/Home/')