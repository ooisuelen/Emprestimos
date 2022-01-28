from django.db import models
from django.db.models import manager

# Create your models here.


class Categoria(models.Model):
    nome = models.CharField(max_length=50)

    def __str__(self):
        return self.nome


class Objeto(models.Model):
    emprestado = models.BooleanField(default=False)
    categoria = models.ForeignKey(Categoria, on_delete=models.PROTECT)
    descricao = models.CharField(max_length=50, verbose_name="Descrição")
    informacoes_adcionais = models.CharField(max_length=50, verbose_name="Informações Adcionais")

    def __str__(self):
        return self.emprestado + ' - ' + str(self.categoria) + ' - ' + str(self.descricao) + ' - ' + str(self.informacoes_adcionais)


class Emprestimo(models.Model):
    data_retirada = models.DateField(verbose_name="Data da Retirada")
    data_limite = models.DateField(verbose_name="Data Limite")
    data_devolucao = models.DateField(verbose_name="Data da Devolução")
    objeto_emprestado = models.ForeignKey(Objeto, on_delete=models.PROTECT, verbose_name="Objeto Emprestado")
    usuario = models.CharField(max_length=50, verbose_name="Usuário")

    def __str__(self):
        return self.data_retirada + ' - ' + str(self.data_limite) + ' - ' + str(self.data_devolucao) + ' - ' + str(self.objeto_emprestado)


class Perfil(models.Model):
    nome = models.CharField(max_length=50, verbose_name="Nome")
    sobrenome = models.CharField(max_length=50, verbose_name="Sobrenome")
    dt_nascimento = models.DateField(verbose_name="Data de Nascimento")
    cpf = models.CharField(max_length=50, verbose_name="CPF")
    ra = models.CharField(max_length=50, verbose_name="RA")
    usuario = models.CharField(max_length=50, verbose_name="Usuário")

    def __str__(self):
        return self.nome + ' - ' + str(self.sobrenome) + ' - ' + str(self.dt_nascimento) + ' - ' + str(self.cpf) + ' - ' + str(self.ra)


class Multa(models.Model):
    valor = models.DecimalField(max_digits=6, decimal_places=2)
    data_multa = models.DateField(verbose_name="Data da Multa", auto_now_add=True)
    data_limite = models.DateField(verbose_name="Data da Multa")
    pagou = models.BooleanField(verbose_name="Pago")

    def __str__(self):
        return self.valor + ' - ' + str(self.data_multa) + ' - ' + str(self.pagou)
