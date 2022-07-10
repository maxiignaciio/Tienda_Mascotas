from django.urls import path, include
from . import views
from .views import RegistroUsuario, UserList
from django.contrib.auth.views import LoginView
from django.contrib.auth import views as auth_views
from django.views.generic import TemplateView

from Usuario import views
from Usuario.views import login

urlpatterns = [
    
    # localhost:8000/usuario/registrar
    path('registrar', RegistroUsuario.as_view(), name="registrar"),
    path('listar', UserList.as_view(), name="list_user"),
    
    path('login/', auth_views.LoginView.as_view(template_name='Usuario/menu_login.html'), name="menu_login"),
    path('sobre_nosotros', TemplateView.as_view(template_name='Paginas/sobre_nosotros.html'), name='sobre_nosotros'),
    path('correa_arena', TemplateView.as_view(template_name='Paginas/pagina_correa_arena.html'), name='correa_arena'),
    path('cama_sofa_azul', TemplateView.as_view(template_name='Paginas/pagina_cama_sofa_azul.html'), name='cama_sofa_azul'),
    path('collar', TemplateView.as_view(template_name='Paginas/pagina_collar.html'), name='collar'),
    path('plato_nordico', TemplateView.as_view(template_name='Paginas/plato_nordico.html'), name='plato_nordico'),
    path('peluches_juguetes', TemplateView.as_view(template_name='Paginas/peluches_juguetes.html'), name='peluches_juguetes'),
    path('collar_bandana', TemplateView.as_view(template_name='Paginas/collar_bandana.html'), name='collar_bandana'),
    path('login', login, name='login'),
]  
