from django.shortcuts import render
from .models import Mascota
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, TemplateView
from django.urls import reverse_lazy
from .forms import MascotaForm
#------------- importacines API ---------------------
from django.http import HttpResponse
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from .serializers import MascotasSerializer
from django.shortcuts import render, redirect, get_object_or_404
from rest_framework import status
from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser 
from django.views.decorators.csrf import csrf_exempt
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated


#=============== API REST ===========================
# El decorador @api_view verifica que la solicitud HTTP apropiada 
# se pase a la función de vista. En este momento, solo admitimos solicitudes GET
@csrf_exempt
@api_view(['GET', 'POST'])
@permission_classes((IsAuthenticated,))
def mascotas_collection(request):
    if request.method == 'GET':
        mascotas = Mascota.objects.all()
        serializer = MascotasSerializer(mascotas, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = MascotasSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            # Si el proceso de deserialización funciona, devolvemos una respuesta con un código 201 (creado
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        # si falla el proceso de deserialización, devolvemos una respuesta 400
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)




@api_view(['GET', 'PUT', 'DELETE'])
@permission_classes((IsAuthenticated,))
def mascotas_element(request, pk):
    mascota = get_object_or_404(Mascota, id=pk)

    if request.method == 'GET':
        serializer = MascotasSerializer(mascota)
        return Response(serializer.data)
    elif request.method == 'DELETE':
        mascota.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
    elif request.method == 'PUT': 
        mascota_new = JSONParser().parse(request) 
        serializer = MascotasSerializer(mascota, data=mascota_new) 
        if serializer.is_valid(): 
            serializer.save() 
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class MascotaCreate(CreateView):
    model = Mascota
    form_class = MascotaForm
    template_name = 'Mascota/mascota_form.html'
    success_url = reverse_lazy("add_mascotas")

class MascotaAdoList(ListView):
    model = Mascota
    template_name = "Mascota/mascotas_adopcion.html"

class MascotaList(ListView):
    model = Mascota
    template_name = 'Mascota/list_mascotas.html'
    

class MascotaUpdate(UpdateView):
    model = Mascota
    form_class = MascotaForm
    template_name = 'Mascota/mascota_form.html'
    success_url = reverse_lazy('list_mascotas')

class MascotaDelete(DeleteView):
    model = Mascota
    template_name = 'Mascota/mascota_delete.html'
    success_url = reverse_lazy('list_mascotas')
    


class MascotaView(TemplateView):
    template_name = "Mascota/mascotas_adopcion.html"