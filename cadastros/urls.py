from django.urls import path
from cadastros.views import lista_cidades, detalhe_cidade, cadastra_cidade, editar_cidade, remove_cidade

urlpatterns = [
    path('', lista_cidades, name='cidades-list'),
    path('detail/<int:id>/', detalhe_cidade, name='cidades-detalhe'),
    path('delete/<int:id>/', remove_cidade, name='cidade-remove'),
    path('create', cadastra_cidade, name='cadastra-cidade'),
    path('update/<int:id>/', editar_cidade, name='edita-cidade'),
]
