from django.db import models

# Create your models here.

class Tarefa(models.Model):
    nome = models.CharField(max_length=100)
    categoria = models.CharField(max_length=100)
    estado = models.BooleanField(default=False)
    def __str__(self):
        return self.nome
