from django.shortcuts import render
from django.urls import reverse_lazy
from .models import Categoria, Objeto, Emprestimo, Perfil, Multa
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.list import ListView
from django.contrib.auth.mixins import LoginRequiredMixin


# Create your views here.

########CRIAR/INSERIR#######
class CategoriaCreate(LoginRequiredMixin, CreateView):
    model = Categoria
    fields = ["nome"]
    template_name = "cadastros/form.html"
    success_url = reverse_lazy("listar-categoria")
    login_url = reverse_lazy('login')


class ObjetoCreate(LoginRequiredMixin, CreateView):
    model = Objeto
    fields = ["emprestado", "categoria", "descricao", "informacoes_adcionais"]
    template_name = "cadastros/form.html"
    success_url = reverse_lazy("listar-objeto")
    login_url = reverse_lazy('login')


class EmprestimoCreate(LoginRequiredMixin, CreateView):
    model = Emprestimo
    fields = ["data_retirada", "data_limite", "data_devolucao", "objeto_emprestado", "usuario"]
    template_name = "cadastros/form.html"
    success_url = reverse_lazy("listar-emprestimo")
    login_url = reverse_lazy('login')


class PerfilCreate(LoginRequiredMixin, CreateView):
    model = Perfil
    fields = ["nome", "sobrenome","dt_nascimento", "cpf", "ra", "usuario"]
    template_name = "cadastros/form.html"
    success_url = reverse_lazy("listar-perfil")
    login_url = reverse_lazy('login')


class MultaCreate(LoginRequiredMixin, CreateView):
    model = Multa
    fields = ["valor", "data_multa", "pagou"]
    template_name = "cadastros/form.html"
    success_url = reverse_lazy("listar-multa")
    login_url = reverse_lazy('login')


#######ATUALIZAR/ALTERAR#######
class CategoriaUpdate(LoginRequiredMixin, UpdateView):
    model = Categoria
    fields = ["nome"]
    template_name = "cadastros/form.html"
    success_url = reverse_lazy("listar-categoria")
    login_url = reverse_lazy('login')


class ObjetoUpdate(LoginRequiredMixin, UpdateView):
    model = Objeto
    fields = ["emprestado", "categoria", "descricao", "informacoes_adcionais"]
    template_name = "cadastros/form.html"
    success_url = reverse_lazy("listar-objeto")
    login_url = reverse_lazy('login')


class EmprestimoUpdate(LoginRequiredMixin, UpdateView):
    model = Emprestimo
    fields = ["data_retirada", "data_limite", "data_devolucao", "objeto_emprestado", "usuario"]
    template_name = "cadastros/form.html"
    success_url = reverse_lazy("listar-emprestimo")
    login_url = reverse_lazy('login')


class PerfilUpdate(LoginRequiredMixin, UpdateView):
    model = Perfil
    fields = ["nome", "sobrenome","dt_nascimento", "cpf", "ra", "usuario"]
    template_name = "cadastros/form.html"
    success_url = reverse_lazy("listar-perfil")
    login_url = reverse_lazy('login')


class MultaUpdate(LoginRequiredMixin, UpdateView):
    model = Multa
    fields = ["valor", "data_multa", "pagou"]
    template_name = "cadastros/form.html"
    success_url = reverse_lazy("listar-multa")
    login_url = reverse_lazy('login')


######DELETAR######
class CategoriaDelete(LoginRequiredMixin, DeleteView):
    model = Categoria
    template_name = "cadastros/form-excluir.html"
    success_url = reverse_lazy("listar-categoria")
    login_url = reverse_lazy('login')


class ObjetoDelete(LoginRequiredMixin, DeleteView):
    model = Objeto
    template_name = "cadastros/form-excluir.html"
    success_url = reverse_lazy("listar-objeto")
    login_url = reverse_lazy('login')


class EmprestimoDelete(LoginRequiredMixin, DeleteView):
    model = Emprestimo
    template_name = "cadastros/form-excluir.html"
    success_url = reverse_lazy("listar-emprestimo")
    login_url = reverse_lazy('login')


class PerfilDelete(LoginRequiredMixin, DeleteView):
    model = Perfil
    template_name = "cadastros/form-excluir.html"
    success_url = reverse_lazy("listar-perfil")
    login_url = reverse_lazy('login')


class MultaDelete(LoginRequiredMixin, DeleteView):
    model = Multa
    template_name = "cadastros/form-excluir.html"
    success_url = reverse_lazy("listar-multa")
    login_url = reverse_lazy('login')


########LISTAR#########
class CategoriaList(LoginRequiredMixin, ListView):
    model = Categoria
    template_name = "cadastros/listas/categoria.html"
    login_url = reverse_lazy('login')


class ObjetoList(LoginRequiredMixin, ListView):
    model = Objeto
    template_name = "cadastros/listas/objeto.html"
    login_url = reverse_lazy('login')


class EmprestimoList(LoginRequiredMixin, ListView):
    model = Emprestimo
    template_name = "cadastros/listas/emprestimo.html"
    login_url = reverse_lazy('login')


class PerfilList(LoginRequiredMixin, ListView):
    model = Perfil
    template_name = "cadastros/listas/perfil.html"
    login_url = reverse_lazy('login')


class MultaList(LoginRequiredMixin, ListView):
    model = Multa
    template_name = "cadastros/listas/multa.html"
    login_url = reverse_lazy('login')

   
