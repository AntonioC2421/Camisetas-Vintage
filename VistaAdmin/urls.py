from VistaAdmin import views
from django.urls import path

urlpatterns = [
    path('ViewAdmin/',views.MainPrincipal, name='PrincipalAdmin'),
]