from django.db import models
from django.db.models import Q, F
from livro.models import Livro
from customUser.models import CustomUser



class Emprestimo(models.Model):
    livro_id = models.ForeignKey(Livro, on_delete=models.CASCADE)
    user_id = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    data_emprestimo = models.DateField()
    data_devolucao = models.DateField()


    class Meta:
        constraints = [
            models.CheckConstraint(
                check=Q(data_devolucao__gte=F('data_emprestimo')),
                name='devolucao_nao_menor_emprestimo'
            )
        ]
