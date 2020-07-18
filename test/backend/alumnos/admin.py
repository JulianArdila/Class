from django.contrib import admin
from .models import Alumno, Classroom, Ciudad

admin.site.register(Alumno)
admin.site.register(Classroom)
admin.site.register(Ciudad)