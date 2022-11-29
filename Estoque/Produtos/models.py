from django.db import models

from Local.models import Local
from Categoria.models import Categoria
from Fornecedor.models import Fornecedor
from Status.models import Status

# Create your models here.

class Produto(models.Model):
    id = models.AutoField(primary_key = True, unique = True)
    nome = models.CharField(max_length = 100, null = False)
    quantidade = models.IntegerField ()
    local = models.ForeignKey(Local, on_delete = models.RESTRICT)
    fornecedor = models.ForeignKey (Fornecedor, on_delete=models.RESTRICT)
    categoria = models.ForeignKey (Categoria, on_delete=models.RESTRICT)
    status = models.ForeignKey(Status, on_delete=models.RESTRICT)