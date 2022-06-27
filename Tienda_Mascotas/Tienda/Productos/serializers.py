from rest_framework import serializers
from .models import Producto

class ProductosSerializer(serializers.ModelSerializer):

    class Meta:
        model = Producto
        fields = ('nombre', 'stock', 'descripcion', 'precio')
