from VistaAdmin import views
from django.urls import path

app_name = 'ViewsAdmin'
urlpatterns = [
    path('ViewAdmin/',views.MainPrincipal, name='PrincipalAdmin'),
    path('ViewAdmin/AddCamiseta/', views.ADDcamisetas, name='ADDcamisetas'),
    path('ViewAdmin/AddCamiseta/ADDimg/<int:id>', views.ADDimgCamiseta, name='ADDimgcamisetas'),
    path('ViewAdmin/AddCamiseta/DeleteImg/<int:img_id>', views.DeleteImg, name='DeleteImg'),
    path('ViewAdmin/AddCamiseta/DeleteTeam/<int:id_team>', views.DeleteTeam, name='DeleteTeam'),
    path('ViewAdmin/AddCamiseta/ChangeInfo/<int:id_team>', views.ChangeInfoCamiseta, name='ChangeInfo'),
    path('exit/', views.exit, name='exit'),
]