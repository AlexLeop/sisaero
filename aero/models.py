from django.db import models


class Cadastros(models.Model):
    matricula = models.IntegerField(verbose_name="MATRÍCULA", null=True, blank=True)
    nome_pessoa = models.CharField(max_length=100, verbose_name="NOME PESSOA", null=True, blank=True)
    posto = models.CharField(max_length=50, verbose_name="POSTO", null=True, blank=True)
    sigla_uo = models.CharField(max_length=20, verbose_name="SIGLA UO", null=True, blank=True)
    data_admissao = models.DateField(verbose_name="DATA ADMISSÃO", null=True, blank=True)
    data_termino = models.DateField(null=True, blank=True, verbose_name="DATA TÉRMINO")
    cpf_pessoa = models.CharField(max_length=14, unique=True, verbose_name="CPF PESSOA", null=True, blank=True)
    banco = models.CharField(max_length=50, verbose_name="BANCO", null=True, blank=True)
    agencia = models.CharField(max_length=20, verbose_name="AGÊNCIA", null=True, blank=True)
    tipo_conta = models.CharField(max_length=20, verbose_name="TIPO CONTA", null=True, blank=True)
    numero_conta = models.CharField(max_length=20, verbose_name="Nº CONTA", null=True, blank=True)
    proventos = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="PROVENTOS", null=True, blank=True)
    descontos = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="DESCONTOS", null=True, blank=True)
    liquido = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="LÍQUIDO", null=True, blank=True)

    def __str__(self):
        return f"{self.nome_pessoa} ({self.matricula})"

