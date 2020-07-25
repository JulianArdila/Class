from rest_framework import serializers
from alumnos.models import Alumno
from drf_extra_fields.fields import Base64ImageField, Base64FileField

class AlumnoSerializer(serializers.ModelSerializer):
    
    imagen = Base64ImageField(required=False)
    #cc_file = Base64FileField()

    class Meta:
        model = Alumno
        fields = ('estado','nombre','codigo','curso','id','ciudad','imagen','escuela')