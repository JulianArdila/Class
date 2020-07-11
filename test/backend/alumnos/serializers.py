from rest_framework import serializers
from alumnos.models import Alumno

class AlumnoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Alumno
        fields = ('estado','nombre','codigo','curso','id','ciudad')