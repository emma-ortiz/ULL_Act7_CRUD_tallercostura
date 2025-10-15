from django.db import models

# Create your models here.
class Profesores(models.Model):
    nombre=models.CharField(max_length=50)
    apellido_paterno=models.CharField(max_length=50)
    apellido_materno=models.CharField(max_length=50)
    genero=models.CharField(max_length=10)
    correo=models.EmailField()

    def __str__(self):
        return self.nombre