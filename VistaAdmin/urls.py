from VistaAdmin import views
from django.urls import path

app_name = 'ViewsAdmin'
urlpatterns = [
    path('ViewAdmin/',views.MainPrincipal, name='PrincipalAdmin'),
    path('ViewAdmin/AddCamiseta/', views.ADDcamisetas, name='ADDcamisetas'),
    path('exit/', views.exit, name='exit'),
]