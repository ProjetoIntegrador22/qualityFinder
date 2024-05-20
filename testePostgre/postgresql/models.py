from django.db import models

# Create your models here.


class Planos(models.Model):
    nome = models.CharField(max_length=100)
    preco = models.DecimalField(max_digits=10, decimal_places=2)
    velocidade = models.DecimalField(max_digits=4, decimal_places=0)
    observacao = models.CharField(max_length=100)
    url = models.CharField(max_length=200, null=True)
    apelido = models.CharField(max_length=50)
    fibra = models.BooleanField()
    satelite = models.BooleanField()

    def __str__(self):
        return self.nome

class Provedor(models.Model):
    planos = models.ManyToManyField(Planos)
    nome = models.CharField(max_length=100)
    apelido = models.CharField(max_length=100)
    cnpj = models.DecimalField(max_digits=14, decimal_places=0)
    

    def __str__(self):
        return self.apelido