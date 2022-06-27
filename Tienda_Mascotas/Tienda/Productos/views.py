from django.shortcuts import render
from .models import Producto
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .forms import ProductoForm

#------------- importacines API ---------------------
from django.http import HttpResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import ProductosSerializer
from django.shortcuts import render, redirect, get_object_or_404
from rest_framework import status
from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser 

#----- API






#=============== API REST ===========================
# El decorador @api_view verifica que la solicitud HTTP apropiada 
# se pase a la función de vista. En este momento, solo admitimos solicitudes GET
@api_view(['GET', 'POST'])
def productos_collection(request):
    if request.method == 'GET':
        productos = Producto.objects.all()
        serializer = ProductosSerializer(productos, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = ProductosSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            # Si el proceso de deserialización funciona, devolvemos una respuesta con un código 201 (creado
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        # si falla el proceso de deserialización, devolvemos una respuesta 400
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)




@api_view(['GET', 'PUT', 'DELETE'])
def productos_element(request, pk):
    producto = get_object_or_404(Producto, id=pk)

    if request.method == 'GET':
        serializer = ProductosSerializer(producto)
        return Response(serializer.data)
    elif request.method == 'DELETE':
        producto.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
    elif request.method == 'PUT': 
        producto_new = JSONParser().parse(request) 
        serializer = ProductosSerializer(producto, data=producto_new) 
        if serializer.is_valid(): 
            serializer.save() 
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ProductoCreate(CreateView):
    model = Producto
    form_class = ProductoForm
    template_name = 'Producto/producto_form.html'
    success_url = reverse_lazy("add_productos")

class ProductoList(ListView):
    model = Producto
    template_name = 'Producto/list_productos.html'
    

class ProductoUpdate(UpdateView):
    model = Producto
    form_class = ProductoForm
    template_name = 'Producto/producto_form.html'
    success_url = reverse_lazy('list_productos')

class ProductoDelete(DeleteView):
    model = Producto
    template_name = 'Producto/producto_delete.html'
    success_url = reverse_lazy('list_productos')



