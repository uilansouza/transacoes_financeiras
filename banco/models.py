from django.db import models
from django.utils import timezone

# Create your models here.
class Transacao(models.Model):
    banco_origem = models.CharField(max_length=30, null=False)
    agencia_origem = models.CharField(max_length=4, null=False)
    conta_origem = models.CharField(max_length=7, null=False)
    banco_destino = models.CharField(max_length=30, null=False)
    agencia_destino = models.CharField(max_length=4, null=False)
    conta_destino = models.CharField(max_length=7, null=False)
    valor_transacao = models.DecimalField(max_digits=8, decimal_places=2)
    data_hora_trasacao = models.DateTimeField(default=timezone.now)
    data_importacao = models.DateTimeField(auto_now=True, verbose_name='Atualizado em')

    def __str__(self):
        return f"{self.banco_origem} -> {self.banco_destino}"
