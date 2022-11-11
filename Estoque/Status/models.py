from django.db import models

OPCOES = (
    {"LIVRE", "Livre"},
    {"MANUTENÇÃO", "Manutenção"},
    {"ESTRAGADO", "Estragado"},
    {"OCUPADO", "Ocupado"},
)

# Create your models here.

class Status(models.Model):
    id = models.AutoField(primary_key=True, unique=True)
    tipo = models.CharField(max_length=10,
                            choices = OPCOES,
                            default = "LIVRE")