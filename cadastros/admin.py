from django.contrib import admin
from .models import Categoria, Objeto, Emprestimo, Perfil, Multa 
# Register your models here.

admin.site.register(Categoria)
admin.site.register(Objeto)
admin.site.register(Emprestimo)
admin.site.register(Perfil)
admin.site.register(Multa)


