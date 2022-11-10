from django.db import models

# Create your models here.

class Categoria(models.Model):
    id = models.AutoField(primary_key=True, unique=True)
    nome = models.CharField(max_length=100)