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

def ADDimgCamiseta(request, id):
    team = Teams.objects.get(id=id)
    addimgform = ADDimgCamisetas()
    imgsTeam = TeamsImgs.objects.filter(teams=id)
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

def DeleteImg(request, teams_id, img_id):
    img = TeamsImgs.objects.get(id=img_id)
    img.delete()
    return redirect('ViewsAdmin:ADDimgCamisetas', teams_id=teams_id)

def exit(request):
    logout(request)
    return redirect('/Home/')