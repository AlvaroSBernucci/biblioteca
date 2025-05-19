from django.contrib import admin
from emprestimo.models import Emprestimo

class EmprestimoAdmin(admin.ModelAdmin):
    list_display = ("livro_id","user_id", "data_emprestimo", "data_devolucao")

admin.site.register(Emprestimo, EmprestimoAdmin)
