from django.contrib import admin
from autor.models import Autor


class AutorAdmin(admin.ModelAdmin):
    list_display = ("nome", "data_nascimento")

admin.site.register(Autor, AutorAdmin)
