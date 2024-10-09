from VistaCliente import views
from django.urls import path


app_name = 'ViewsClient'
urlpatterns = [
    path('', views.MainPrincipalCliente, name='MainPrincipalCliente'),
    path('ViewCamisetas/<int:id>/', views.ViewCamisetas, name='ViewsCamiset'),
    path('ViewCamisetas/<int:id>/<int:team_id>/', views.ViewCamisetas, name='ViewsCamisetTeam'),
    path('DataCamiset/<int:id>' ,views.DetalleCamiseta, name="DetalleCamiseta"),
    path('Search/', views.Search, name='Search'),
    path('DeleteItemCart/<int:id_item>', views.DeleteItemsCart, name='DeleteItem'),
    path('ValidCod/<str:cod_pro>', views.ValidacionCod, name='ValidacionCodigoURL'),
    path('AddVenta/', views.Realizar_Venta, name='AddVenta'),
    path('ItemsCart/', views.ViewItemsCart, name='ItemsCart'),
]