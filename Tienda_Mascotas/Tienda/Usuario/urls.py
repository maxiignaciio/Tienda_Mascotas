from django.urls import path, include
from . import views
from .views import RegistroUsuario, UserList
from django.contrib.auth.views import LoginView
from django.contrib.auth import views as auth_views


urlpatterns = [
    
    # localhost:8000/usuario/registrar
    path('registrar', RegistroUsuario.as_view(), name="registrar"),
    path('listar', UserList.as_view(), name="list_user"),
    
    path('login/', auth_views.LoginView.as_view(template_name='Usuario/login.html'), name='login'),
    path('pruebalogin/', auth_views.LoginView.as_view(template_name='Usuario/menu_login.html'), name='prueba-login'),
]  
