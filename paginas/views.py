from django.views.generic import TemplateView


class PaginaInicial(TemplateView):
    template_name = 'paginas/index.html'

class Sobre(TemplateView):
    template_name = 'paginas/sobre.html'

class Cadastro(TemplateView):
    template_name = 'paginas/cadastro.html'

  
