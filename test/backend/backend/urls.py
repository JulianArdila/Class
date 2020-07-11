"""backend URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from alumnos.views import principal, principalajax
from django.conf.urls import url, include

urlV2 = [
    url(r'^', include(('alumnos.urls','alumnos'))),
    url(r'^', include(('user.urls','user'))),
]


urlpatterns = [
    path('admin/', admin.site.urls),
    url('api/', include('rest_auth.urls')),
    path('principal/', principal),
    url('v2/',include(urlV2)),
    url('principalajax/', principalajax),
]
