from django.db import models

# Create your models here.
class Alumno(models.Model):
    nombre = models.CharField(max_length=150,blank=False)
    edad = models.IntegerField()
    sexo =  models.CharField(max_length=1)

    def __str__(self):
        texto = " {0} - {1} - {2} "
        return texto.format(self.nombre,self.edad,self.sexo)
    
