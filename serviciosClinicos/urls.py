"""serviciosClinicos URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
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
from django.urls import path, include
from serviciosClinicos import views



urlpatterns = [

    
    path('', views.bienvenida , name = 'bienvenida'),

    path('base' , views.base , name = 'base'),

    path('diseñobasico' , views.baseNormal , name = 'baseNormal'),

    path('Usuarios/', include('Usuarios.urls')),
    path('Usuarios/', include('django.contrib.auth.urls')),
    
    
    path('serviciosClinicos/',include('aperturaNinos.urls')),
    
    path('serviciosClinicos/',include('aperturaAdultos.urls')),
    
    path('serviciosClinicos/',include('Fonoaudiologia.urls')),
    
    path('serviciosClinicos/',include('Neuropsicologia.urls')),
    
    path('serviciosClinicos/',include('Fisioterapia.urls')),
    
    path('serviciosClinicos/',include('Psicologia.urls')),
    
    path('serviciosClinicos/',include('PsicologiaMenores.urls')),
    
    path('serviciosClinicos/',include('Psiquiatria.urls')),
    
    path('serviciosClinicos/',include('TerapiaOcupacional.urls')),


    path('admin/', admin.site.urls),
    
   
]
