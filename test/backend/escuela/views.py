from django.shortcuts import render
from rest_framework import generics
from .serializers import EscuelaSerializer
from .models import Escuela
# Create your views here.

class EscuelaList(generics.ListCreateAPIView):
    serializer_class = EscuelaSerializer
    queryset = Escuela.objects.all()

class EscuelaDetail(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = EscuelaSerializer
    queryset = Escuela.objects.all()
