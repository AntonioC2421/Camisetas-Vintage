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
    path('ViewAdmin/AddDatos/', views.ViewDatos.viewsAgregarDatos, name='AddDatos'),
    path('DeleteDato/<int:id_dato>/', views.ViewDatos.eliminar_datos, name='delete_marca'),
    path('loginVintage/',views.redirigir_usuario, name='redirigir_usuario'),
    path('RegistrationUser/', views.ViewsAddCliente, name='CreateUser'),
<<<<<<< HEAD
    path('AddItemCart/', views.AddItemCart, name='AddItemsCart'),
=======
>>>>>>> ab94e0bb148cb187ec9f7249ad53c2663e161111
    path('exit/', views.exit, name='exit'),
]
