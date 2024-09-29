from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('AdminView/',include('VistaAdmin.urls')),
    path('Home/',include('VistaCliente.urls')),
    path('accounts/',include('django.contrib.auth.urls')),
    # URL para restablecer contraseña
    path('password_reset/', auth_views.PasswordResetView.as_view(
        template_name='authentication/ResetPassword.html'),
        name='password_reset'),       

    path('password_reset/done/', auth_views.PasswordResetDoneView.as_view(
        template_name='authentication/SentPassword.html'),
        name='password_reset_done'),
    
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(
        template_name='authentication/PasswordResetConfirm.html'),
        name='password_reset_confirm'),
    
    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(
        template_name='authentication/PasswordResetComplete.html'),
        name='password_reset_complete'),
]+ static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)