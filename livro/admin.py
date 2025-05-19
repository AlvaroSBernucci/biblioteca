from django.contrib import admin
from livro.models import Livro

class LivroAdmin(admin.ModelAdmin):
    list_display = ("titulo","descricao","editora","publicado_em","autor_id")


admin.site.register(Livro, LivroAdmin)
