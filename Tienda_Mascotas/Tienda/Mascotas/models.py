from distutils.command.upload import upload
from django.db import models

# Create your models here.
class Mascota(models.Model):
    foto = models.ImageField(upload_to='images/rescatados', blank=True)
    nombre = models.CharField(max_length=20)
    anios = models.IntegerField()
    raza = models.CharField(max_length=20)
    descripcion = models.CharField(max_length=250)
    
    def __str__(self):
        return self.nombre