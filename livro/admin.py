from django.contrib import admin
from livro.models import Livro, Genero

class LivroAdmin(admin.ModelAdmin):
    list_display = ("titulo","descricao","editora","publicado_em","autor_id")


admin.site.register(Livro, LivroAdmin)
admin.site.register(Genero)
