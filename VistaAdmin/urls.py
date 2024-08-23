from VistaAdmin import views
from django.urls import path,include

app_name = 'ViewsAdmin'
urlpatterns = [
    path('ViewAdmin/',views.MainPrincipal, name='PrincipalAdmin'),
    
    path('exit/', views.exit, name='exit'),
]