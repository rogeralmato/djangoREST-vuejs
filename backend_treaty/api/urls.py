from django.urls import path
from .views import UsuarioList

urlpatterns = [
    path('usuario/all', UsuarioList.as_view(), name='usario_list'),
]
