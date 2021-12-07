from django.contrib import admin
from cadastros.models import Cidade, Pais, Estado


class EstadoInLine(admin.TabularInline):
    model = Estado


class PaisAdmin(admin.ModelAdmin):
    fields = ('nome',)
    inlines = [
        EstadoInLine
    ]

admin.site.register(Pais, PaisAdmin)
admin.site.register(Estado)
admin.site.register(Cidade)
