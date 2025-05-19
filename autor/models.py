from django.db import models

class Autor(models.Model):
    nome = models.CharField(max_length=30, blank=False)
    data_nascimento = models.DateField()

    def __str__(self):
        return self.nome
