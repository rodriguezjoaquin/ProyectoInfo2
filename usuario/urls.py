from django.urls import path
from usuario import views as usuario_views
from usuario.views import registro, login, logout, home

urlpatterns = [
    path('registro', registro),#usuario_views.registro
    path('login', login),
    path('logout', logout),
    path('', home),
]