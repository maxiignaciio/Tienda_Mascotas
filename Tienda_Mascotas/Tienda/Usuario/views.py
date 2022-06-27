from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.views.generic import CreateView
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView
from .forms import RegistroForm

from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token
from django.conf import settings
# from django.contrib.auth.models import User

# @receiver(post_save, sender=User)
# def create_auth_token(sender, instance=None, created=False, **kwargs):
#     if created:
#         Token.objects.create(user=instance)
        
# Este código se activa cada vez que se 
# crea un nuevo usuario y se guarda en la base de datos.
@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)


class RegistroUsuario(CreateView):
    model = User
    template_name = "Usuario/usuario_form.html"
    form_class = RegistroForm
    success_url = reverse_lazy('home')


class UserList(ListView):
    model = User
    template_name = 'Usuario/listar_usuario.html'

