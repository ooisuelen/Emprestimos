from os import name
from django.urls import path
from .views import PaginaInicial, Sobre, Cadastro

urlpatterns = [
    # Criar todos os endereços/rotas
    # path('endereço/', MinhaView.as_view(), name='referência/apelido'),
    
    path('', PaginaInicial.as_view(), name='index'),
    path('sobre/', Sobre.as_view(), name='sobre'),


    
]
