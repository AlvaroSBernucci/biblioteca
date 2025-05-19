from django.db import models
from autor.models import Autor

class Livro(models.Model):
    titulo = models.CharField(max_length=50, blank=False)
    descricao = models.CharField(max_length=255)
    editora = models.CharField(max_length=30)
    publicado_em = models.DateField()
    autor_id = models.ForeignKey(Autor, on_delete=models.CASCADE)


    def __str__(self):
        return self.titulo
