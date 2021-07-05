from django.contrib import admin
from estoque.models import produto


# Register your models here.
@admin.register(produto)
class produtoadmin(admin.ModelAdmin):
    list_display = ('nome', 'tem_desconto', 'porcentagem_desconto',
                    'preco', 'preco_desconto', 'imagem', 'descricao', 'loja')
