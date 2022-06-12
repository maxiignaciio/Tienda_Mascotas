from django.db import models

# Create your models here.
class Producto(models.Model):
    nombre = models.CharField(max_length=20)
    stock = models.IntegerField()
    descripcion = models.CharField(max_length=250)
    precio = models.IntegerField()
    
    def __str__(self):
        return self.nombre

