from django.db import models
from django.contrib.auth.admin import User


class UsuarioPersonalizado(models.Model):
    """
    usuarios do sistema com campos personalizados
    """
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.usuario
