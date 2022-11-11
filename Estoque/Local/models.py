from django.db import models

# Create your models here.

class Local(models.Model):
    id = models.AutoField(primary_key=True, unique=True)
    sala = models.CharField(max_length=100, null=False)
    armario = models.CharField(max_length=100)
    numero = models.CharField(max_length=10)