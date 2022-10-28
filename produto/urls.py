from django.urls import path
from . import views

app_name = 'produto'  # namespace

urlpatterns = [
    path('', views.ListaProdutos.as_view(), name='lista'),
    path('<slug>', views.DetalheProduto.as_view(), name='detalhe'),
    path('adicionaraocarrinho/', views.AdicionaraoCarrinho.as_view(),
         name='adicionaraocarrinho'),
    path('removerdocarrinho/', views.RemoverdoCarrinho.as_view(),
         name='removerdocarrinho'),
    path('carrinho/', views.Carrinho.as_view(), name='carrinho'),
    path('resumodacompra/', views.ResumodaCompra.as_view(), name='resumodacompra'),
    path('busca/', views.Busca.as_view(), name='busca'),
]
