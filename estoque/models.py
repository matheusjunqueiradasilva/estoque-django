from django.db import models

# Create your models here.


class produto (models.Model):
    nome = models.CharField(max_length=50, null=False, blank=False)
    tem_desconto = models.BooleanField('desconto')
    porcentagem_desconto = models.IntegerField('porcentagem')

    preco = models.FloatField(max_length=500, null=False, blank=False)

    def preco_desconto(self):
        if self.tem_desconto:
            return self.preco - (self.preco * (self.porcentagem_desconto/100))
        else:
            return self.preco

    def __str__(self) -> str:
        return self.nome

    imagem = models.ImageField(null=False, blank=False)
    descricao = models.TextField(null=False, blank=False)
    loja = models.CharField(max_length=30, null=False, blank=False)
