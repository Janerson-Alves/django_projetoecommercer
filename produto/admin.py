from django.contrib import admin
from . import models


class VariacaoInline(admin.TabularInline):  # tabulação da variação
    model = models.Variacao
    extra = 1


class ProdutoAdmin(admin.ModelAdmin):  # aparecer na tela do Produto
    list_display = [
        'nome', 'descricao_curta', 'get_preco_formatado', 'get_preco_promocional_formatado'
    ]
    inlines = [
        VariacaoInline
    ]


admin.site.register(models.Produto, ProdutoAdmin)
admin.site.register(models.Variacao)
