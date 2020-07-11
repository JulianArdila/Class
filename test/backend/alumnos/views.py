
from django.shortcuts import render
from alumnos.models import Alumno, Ciudad
from rest_framework import generics
from alumnos.serializers import AlumnoSerializer

class AlumnoList(generics.ListCreateAPIView):
    serializer_class = AlumnoSerializer
    queryset = Alumno.objects.all().filter(estado=1)

class AlumnoDetail(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = AlumnoSerializer
    queryset = Alumno.objects.all()


def principal(request):
    alumnos = Alumno.objects.all()
    result = {
        'alumnos':alumnos,
    }
    num = 2
    concat = r' {num}'
    print(alumnos)
    print(type(alumnos))
    return render(request,"principal.html",  result)

def principalajax(request):
    return render(request,"principalajax.html")