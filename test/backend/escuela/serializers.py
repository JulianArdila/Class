from rest_framework import serializers
from .models import Escuela
from drf_extra_fields.fields import Base64ImageField, Base64FileField

class EscuelaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Escuela
        fields = ('id','nombre')