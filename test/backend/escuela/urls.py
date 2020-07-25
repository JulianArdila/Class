from django.conf.urls import url
from .views import EscuelaList, EscuelaDetail

urlpatterns = [
    url(r'^escuela/$', EscuelaList.as_view()),
    url(r'^escuela/(?P<pk>[0-9]+)/$', EscuelaDetail.as_view()),
]