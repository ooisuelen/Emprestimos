from django.shortcuts import render
from django.urls import reverse_lazy
from .models import Categoria, Objeto, Emprestimo, Perfil, Multa
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.list import ListView

# Create your views here.

########CRIAR/INSERIR#######
class CategoriaCreate(CreateView):
    model = Categoria
    fields = ["nome"]
    template_name = "cadastros/form.html"
    success_url = reverse_lazy("listar-categoria")
class ObjetoCreate(CreateView):
    model = Objeto
    fields = ["emprestado", "categoria", "descricao", "informacoes_adcionais"]
    template_name = "cadastros/form.html"
    success_url = reverse_lazy("listar-objeto")
class EmprestimoCreate(CreateView):
    model = Emprestimo
    fields = ["data_retirada", "data_limite", "data_devolucao", "objeto_emprestado", "usuario"]
    template_name = "cadastros/form.html"
    success_url = reverse_lazy("listar-emprestimo")
class PerfilCreate(CreateView):
    model = Perfil
    fields = ["nome", "sobrenome","dt_nascimento", "cpf", "ra", "usuario"]
    template_name = "cadastros/form.html"
    success_url = reverse_lazy("listar-perfil")
class MultaCreate(CreateView):
    model = Multa
    fields = ["valor", "data_multa", "pagou"]
    template_name = "cadastros/form.html"
    success_url = reverse_lazy("listar-multa")

#######ATUALIZAR/ALTERAR#######
class CategoriaUpdate(UpdateView):
    model = Categoria
    fields = ["nome"]
    template_name = "cadastros/form.html"
    success_url = reverse_lazy("listar-categoria")
class ObjetoUpdate(UpdateView):
    model = Objeto
    fields = ["emprestado", "categoria", "descricao", "informacoes_adcionais"]
    template_name = "cadastros/form.html"
    success_url = reverse_lazy("listar-objeto")
class EmprestimoUpdate(UpdateView):
    model = Emprestimo
    fields = ["data_retirada", "data_limite", "data_devolucao", "objeto_emprestado", "usuario"]
    template_name = "cadastros/form.html"
    success_url = reverse_lazy("listar-emprestimo")
class PerfilUpdate(UpdateView):
    model = Perfil
    fields = ["nome", "sobrenome","dt_nascimento", "cpf", "ra", "usuario"]
    template_name = "cadastros/form.html"
    success_url = reverse_lazy("listar-perfil")
class MultaUpdate(UpdateView):
    model = Multa
    fields = ["valor", "data_multa", "pagou"]
    template_name = "cadastros/form.html"
    success_url = reverse_lazy("listar-multa")

######DELETAR######
class CategoriaDelete(DeleteView):
    model = Categoria
    template_name = "cadastros/form-excluir.html"
    success_url = reverse_lazy("listar-categoria")
class ObjetoDelete(DeleteView):
    model = Objeto
    template_name = "cadastros/form-excluir.html"
    success_url = reverse_lazy("listar-objeto")
class EmprestimoDelete(DeleteView):
    model = Emprestimo
    template_name = "cadastros/form-excluir.html"
    success_url = reverse_lazy("listar-emprestimo")
class PerfilDelete(DeleteView):
    model = Perfil
    template_name = "cadastros/form-excluir.html"
    success_url = reverse_lazy("listar-perfil")
class MultaDelete(DeleteView):
    model = Multa
    template_name = "cadastros/form-excluir.html"
    success_url = reverse_lazy("listar-multa")

########LISTAR#########
class CategoriaList(ListView):
    model = Categoria
    template_name = "cadastros/listas/categoria.html"
class ObjetoList(ListView):
    model = Objeto
    template_name = "cadastros/listas/objeto.html"
class EmprestimoList(ListView):
    model = Emprestimo
    template_name = "cadastros/listas/emprestimo.html"
class PerfilList(ListView):
    model = Perfil
    template_name = "cadastros/listas/perfil.html"
class MultaList(ListView):
    model = Multa
    template_name = "cadastros/listas/multa.html"
   