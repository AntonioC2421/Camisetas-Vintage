from VistaCliente import views
from django.urls import path


app_name = 'ViewsClient'
urlpatterns = [
    path('', views.MainPrincipalCliente, name='MainPrincipalCliente'),
    path('ViewCamisetas/<int:id>/', views.ViewCamisetas, name='ViewsCamiset'),
    path('ViewCamisetas/<int:id>/<int:team_id>/', views.ViewCamisetas, name='ViewsCamisetTeam'),
    path('DataCamiset/<int:id>' ,views.DetalleCamiseta, name="DetalleCamiseta"),
    path('Search/', views.Search, name='Search'),
<<<<<<< HEAD
    path('DeleteItemCart/<int:id_item>', views.DeleteItemsCart, name='DeleteItem'),
=======
    
>>>>>>> ab94e0bb148cb187ec9f7249ad53c2663e161111
]