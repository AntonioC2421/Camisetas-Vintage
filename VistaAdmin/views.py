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

def ADDimgCamisetasViews(request, id):
    Team = Teams.objects.get(id=id)
    TeamMain = Teams.objects.filter(id=id)
    imgsTeam = TeamsImgs.objects.filter(teams=id)
    data = {'FormADDimgCamisetas': ADDimgCamisetas(), 'imgs': imgsTeam, 'imgMain': TeamMain}
    if request.method == 'POST':
        formimgteam = ADDimgCamisetas(request.POST, request.FILES)
        if formimgteam.is_valid():
            if not request.FILES:
                data['mensaje'] = 'Ingrese una imagen'
            else:
                formimgteam_instance = formimgteam.save(commit=False)
                formimgteam_instance.teams = Team
                formimgteam_instance.save()
                return redirect('ViewsAdmin:ADDimgCamisetas' ,id=id)
        data['formimgteam'] = ADDimgCamisetas()
    return render(request, './TemplatesAdmin/ADDcamisetas/ADDimgcamisetas.html', data)

def DeleteImg(request, id):
    img = TeamsImgs.objects.get(id=id)
    teams_id = img.teams.id
    img.delete()
    return redirect('ViewsAdmin:ADDimgCamisetas', id=teams_id)

def exit(request):
    logout(request)
    return redirect('/Home/')