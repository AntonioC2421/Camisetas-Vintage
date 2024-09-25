from VistaAdmin import views
from django.urls import path

app_name = 'ViewsAdmin'
urlpatterns = [
    path('ViewAdmin/', views.MainPrincipal, name='PrincipalAdmin'),
    path('ViewAdmin/AddCamiseta/', views.ADDcamisetas, name='ADDcamisetas'),
    path('ViewAdmin/AddCamiseta/ADDimg/<int:id>', views.ADDimgCamiseta, name='ADDimgcamisetas'),
    path('ViewAdmin/AddCamiseta/DeleteImg/<int:img_id>', views.DeleteImg, name='DeleteImg'),
    path('ViewAdmin/AddCamiseta/DeleteTeam/<int:id_team>', views.DeleteTeam, name='DeleteTeam'),
    path('ViewAdmin/AddCamiseta/ChangeInfo/<int:id_team>', views.ChangeInfoCamiseta, name='ChangeInfo'),
    path('ViewsAdmin/CodiPromo', views.CodiPromoViews, name='CodPromUrl'),
    path('ViewsAdmin/CodiPromo/DeleteCod/<int:id_cod>', views.DeleteCodPromo, name='deletecod'),
    path('ViewAdmin/AddCamiseta/ChangeInfoCod/<int:id_cod>', views.ChangeInfoCod, name='ChangeInfoCod'),
    path('ViewAdmin/AddDatos/', views.ViewDatos.viewsAgregarDatos, name='AddDatos'),  # Asegúrate de esta URL
    path('DeleteDato/<int:id_dato>/', views.ViewDatos.eliminar_datos, name='delete_marca'),
    path('loginVintage/',views.redirigir_usuario, name='redirigir_usuario'),
    path('exit/', views.exit, name='exit'),
]
