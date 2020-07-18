from rest_framework import serializers
from alumnos.models import Alumno
from drf_extra_fields.fields import Base64ImageField

class AlumnoSerializer(serializers.ModelSerializer):
    
    imagen = Base64ImageField()

    class Meta:
        model = Alumno
        fields = ('estado','nombre','codigo','curso','id','ciudad','imagen')