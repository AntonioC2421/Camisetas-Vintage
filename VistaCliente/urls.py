from VistaCliente import views
from django.urls import path
app_name = 'ViewsClient'
urlpatterns = [
    path('',views.MainPrincipalCliente, name='MainPrincipalCliente'),
    path('ViewCamisetas/<int:id>', views.ViewCamisetas, name='ViewsCamiset'),
]