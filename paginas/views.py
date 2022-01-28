from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin


class PaginaInicial(TemplateView):
    template_name = 'paginas/index.html'

class Sobre(TemplateView):
    template_name = 'paginas/sobre.html'

class Cadastro(TemplateView):
    template_name = 'paginas/cadastro.html'

  
