from django.db import models


# Create your models here.
class Cliente(models.Model):


    nome = models.CharField(max_length=150)
    email = models.EmailField(blank=True)
    telefone = models.CharField( max_length=20, blank=True)
    ativo = models.BooleanField(default=True)
    conta = models.ForeignKey(
        "contas.Conta",
        on_delete=models.PROTECT,
        related_name="clientes",
    )
    criado_em = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.nome