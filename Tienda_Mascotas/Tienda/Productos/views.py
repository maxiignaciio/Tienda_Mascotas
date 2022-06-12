from django.shortcuts import render
from .models import Producto
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .forms import ProductoForm

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



