"""
URL configuration for jas_softpy project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from . import views

urlpatterns = [
    path('', views.Index),
    path('admin/', admin.site.urls),
    path('home/', views.home, name='home'),
    path('producto/', views.producto, name='producto'),
    path('ventas/', views.ventas, name='ventas'),
    path('GestionPersonal/', views.GestionPersonal, name='GestionPersonal'),
    path('Postulacion/', views.Postulacion, name='Postulacion'),
    path('ordenpedido/', views.ordenpedido, name='ordenpedido')
]
