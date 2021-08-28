"""proyectoInfo2021 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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

from django.contrib import admin
from django.urls import path, include
from usuario import views as usuario_views
from usuario.views import registro,login,logout,home

urlpatterns = [
    path('admin/', admin.site.urls),
    path('juego/', include('juego.urls')),
    #path('', include('juego.urls'))
    path('registro', usuario_views.registro),
    path('login', usuario_views.login),
    path('logout', usuario_views.logout),
    path('', usuario_views.home),

]

