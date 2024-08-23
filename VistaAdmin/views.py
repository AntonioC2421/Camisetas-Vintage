from django.shortcuts import render
from .models import Categorias
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from django.shortcuts import redirect

#Pagina Principal de el Admin
@login_required
def MainPrincipal(request):
    return render(request, './TemplatesAdmin/Principal/Principal.html')

def exit(request):
    logout(request)
    return redirect('/Home/')