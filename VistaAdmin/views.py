from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from django.shortcuts import redirect
from .forms import *
from .models import *

#Pagina Principal de el Admin
@login_required
def MainPrincipal(request):
    return render(request, './TemplatesAdmin/Principal/Principal.html')

#Sección ADDMINISTRACIÓN DE CAMISETAS
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

#Deslogueo
def exit(request):
    logout(request)
    return redirect('/Home/')