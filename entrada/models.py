from django.db import models
from aero.models import Cadastros


class EntradasAero(models.Model):
    cadastro = models.ForeignKey(Cadastros, on_delete=models.CASCADE, related_name="entradas", verbose_name="CADASTRO")
    org = models.CharField(max_length=6, blank=True, null=True, verbose_name="ORG")
    matricula = models.IntegerField(verbose_name="MATRICULA")
    nome = models.CharField(max_length=50, blank=True, null=True, verbose_name="NOME")
    un_org = models.CharField(max_length=50, blank=True, null=True, verbose_name="UND. ORGANIZACIONAL")
    cargo = models.CharField(max_length=20, blank=True, null=True, verbose_name="CARGO")
    ind_parcs_pg = models.CharField(max_length=20, blank=True, null=True, verbose_name="INDICE DE PARCELAS PAGAS")
    valor = models.BooleanField(max_length=20, blank=True, null=True, verbose_name="VALOR")
    caixas = models.CharField(max_length=120, blank=True, null=True, verbose_name="CAIXAS")

    def __str__(self):
        return self.nome
