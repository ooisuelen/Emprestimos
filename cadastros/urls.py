from os import name
from django.urls import path
from .views import CategoriaCreate, ObjetoCreate, EmprestimoCreate, PerfilCreate, MultaCreate

urlpatterns = [
    # path('endereço', MinhaView.as_view(), name="name-da-url"),

    path("cadastrar/categoria/", CategoriaCreate.as_view(), name="cadastrar-categoria"),

    path("cadastrar/objeto/", ObjetoCreate.as_view(), name="cadastrar-objeto"),

    path("cadastrar/emprestimo/", EmprestimoCreate.as_view(), name="cadastrar-emprestimo"),

    path("cadastrar/perfil/", PerfilCreate.as_view(), name="cadastrar-perfil"),


    path("cadastrar/multa/", MultaCreate.as_view(), name="cadastrar-multa"),
]

