from django.conf.urls import url
from alumnos.views import AlumnoList, AlumnoDetail

urlpatterns = [
    url(r'^alumnos/$', AlumnoList.as_view()),
    url(r'^alumnos/(?P<pk>[0-9]+)/$', AlumnoDetail.as_view()),
]