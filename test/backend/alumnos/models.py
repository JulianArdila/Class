from django.db import models

class Ciudad(models.Model):
    nombre = models.CharField(max_length=200)

    def __str__(self):
        return self.nombre

class Alumno(models.Model):
    # estado 1 activo
    # estado 0 desactivado
    estado = models.IntegerField(default=1)
    nombre = models.CharField(max_length=200)
    codigo = models.CharField(max_length=200)
    #cedula = models.IntegerField(unique=True)
    curso = models.IntegerField()
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    ciudad = models.ForeignKey(Ciudad,on_delete=models.CASCADE,related_name='alumno',null=True, blank=True)
    imagen = models.ImageField(upload_to='Alumnos/', blank=True, null=True)

    def __str__(self):
        return self.nombre


class Classroom(models.Model):
    fecha_creacion = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    
    estudiante = models.ManyToManyField(Alumno, related_name="clase")

    def __str__(self):
        return str(self.fecha_creacion)


