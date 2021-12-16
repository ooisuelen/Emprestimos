from os import name
from django.urls import path
from .views import CategoriaCreate, ObjetoCreate, EmprestimoCreate, PerfilCreate, MultaCreate
from .views import CategoriaUpdate, ObjetoUpdate, EmprestimoUpdate, PerfilUpdate, MultaUpdate
from .views import CategoriaDelete, ObjetoDelete, EmprestimoDelete, PerfilDelete, MultaDelete
from .views import CategoriaList, ObjetoList, EmprestimoList, PerfilList, MultaList


urlpatterns = [
    # path('endereço', MinhaView.as_view(), name="name-da-url"),

    path("cadastrar/categoria/", CategoriaCreate.as_view(), name="cadastrar-categoria"),
    path("cadastrar/objeto/", ObjetoCreate.as_view(), name="cadastrar-objeto"),
    path("cadastrar/emprestimo/", EmprestimoCreate.as_view(), name="cadastrar-emprestimo"),
    path("cadastrar/perfil/", PerfilCreate.as_view(), name="cadastrar-perfil"),
    path("cadastrar/multa/", MultaCreate.as_view(), name="cadastrar-multa"),

    path("editar/categoria/<int:pk>/", CategoriaUpdate.as_view(), name="editar-categoria"),
    path("editar/objeto/<int:pk>/", ObjetoUpdate.as_view(), name="editar-objeto"),
    path("editar/emprestimo/<int:pk>/", EmprestimoUpdate.as_view(), name="editar-emprestimo"),
    path("editar/perfil/<int:pk>/", PerfilUpdate.as_view(), name="editar-perfil"),
    path("editar/multa/<int:pk>/", MultaUpdate.as_view(), name="editar-multa"),

    path("excluir/categoria/<int:pk>/", CategoriaDelete.as_view(), name="excluir-categoria"),
    path("excluir/objeto/<int:pk>/", ObjetoDelete.as_view(), name="excluir-objeto"),
    path("excluir/emprestimo/<int:pk>/", EmprestimoDelete.as_view(), name="excluir-emprestimo"),
    path("excluir/perfil/<int:pk>/", PerfilDelete.as_view(), name="excluir-perfil"),
    path("excluir/multa/<int:pk>/", MultaDelete.as_view(), name="excluir-multa"),

    path("listar/categoria/", CategoriaList.as_view(), name="listar-categoria"),
    path("listar/objeto/", ObjetoList.as_view(), name="listar-objeto"),
    path("listar/emprestimo/", EmprestimoList.as_view(), name="listar-emprestimo"),
    path("listar/perfil/", PerfilList.as_view(), name="listar-perfil"),
    path("listar/multa/", MultaList.as_view(), name="listar-multa"),


]

