from VistaAdmin import views
from django.urls import path

app_name = 'ViewsAdmin'
urlpatterns = [
    path('ViewAdmin/',views.MainPrincipal, name='PrincipalAdmin'),
    path('ViewAdmin/AddCamiseta/', views.ADDcamisetas, name='ADDcamisetas'),
    path('ViewAdmin/AddCamiseta/AddImg/<int:id>', views.ADDimgCamisetasViews, name='ADDimgCamisetas'),
    path('ViewAdmin/AddCamiseta/DeleteImg/<int:id>', views.DeleteImg,name='DeleteImg'),
    path('exit/', views.exit, name='exit'),
]