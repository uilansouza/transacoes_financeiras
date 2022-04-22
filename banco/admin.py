from django.contrib import admin
from banco.models import Transacao

# Register your models here.
class Transacoes(admin.ModelAdmin):
    list_display = ['id', 'banco_origem','banco_destino', 'agencia_destino', 'conta_destino', 'valor_transacao','data_hora_trasacao','data_importacao']
    list_display_links = ['id', 'banco_origem','banco_destino', 'data_hora_trasacao']
    search_fields = ['banco_origem','banco_destino']

admin.site.register(Transacao, Transacoes)