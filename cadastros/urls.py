from django.urls import path
from cadastros.views import lista_cidades, detalhe_cidade, cadastra_cidade

urlpatterns = [

    path('', lista_cidades, name='cidades-list'),
    path('detail/<int:id>/', detalhe_cidade, name='cidades-detalhe'),
    path('create', cadastra_cidade, name='cadastra-cidade'),
]
