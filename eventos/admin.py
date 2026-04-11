"""Configuração do admin para o app de gastos."""

from django.contrib import admin

from .models import Eventos


@admin.register(Eventos)
class EventosAdmin(admin.ModelAdmin):
    list_display = ["descricao", "data_hora", "ciclo"]
    list_filter = ["ciclo", "data_hora"]
    search_fields = ["descricao"]
