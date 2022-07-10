from rest_framework import serializers
from .models import Mascota

class MascotasSerializer(serializers.ModelSerializer):

    class Meta:
        model = Mascota
        fields = ('nombre', 'anios', 'raza', 'descripcion')