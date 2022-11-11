from django.db import models

# Create your models here.

class Fornecedor(models.Model):
    id = models.AutoField(primary_key=True, unique=True)
    nome = models.CharField(max_length=100)
    cnpj = models.CharField(max_length=100)
    endereco = models.CharField(max_length=225)
    telefone = models.CharField(max_length=20)
    email = models.CharField(max_length=100)