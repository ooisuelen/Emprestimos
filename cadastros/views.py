from django.shortcuts import render
from django.urls import reverse_lazy
from .models import Categoria, Objeto, Emprestimo, Perfil, Multa
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.list import ListView

# Create your views here.


class CategoriaCreate(CreateView):
    model = Categoria
    fields = ["nome"]
    template_name = "cadastros/form.html"
    success_url = reverse_lazy("index")


class ObjetoCreate(CreateView):
    model = Objeto
    fields = ["emprestado", "categoria", "descricao", "informacoes_adcionais"]
    template_name = "cadastros/form.html"
    success_url = reverse_lazy("index")


class EmprestimoCreate(CreateView):
    model = Emprestimo
    fields = ["data_retirada", "data_limite", "data_devolucao", "objeto_emprestado", "usuario"]
    template_name = "cadastros/form.html"
    success_url = reverse_lazy("index")


class PerfilCreate(CreateView):
    model = Perfil
    fields = ["nome", "sobrenome","dt_nascimento", "cpf", "ra", "usuario"]
    template_name = "cadastros/form.html"
    success_url = reverse_lazy("index")




class MultaCreate(CreateView):
    model = Multa
    fields = ["valor", "data_multa", "pagou"]
    template_name = "cadastros/form.html"
    success_url = reverse_lazy("index")
