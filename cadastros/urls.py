from django.contrib.auth.decorators import login_required
from django.urls import path
from cadastros.views import CidadeList, CidadeDetail, CidadeDelete, CidadeCreate, CidadeUpdate

urlpatterns = [
    path('', CidadeList.as_view(), name='cidades-list'),
    path('detail/<int:pk>/', CidadeDetail.as_view(), name='cidades-detalhe'),
    path('delete/<int:pk>/', login_required(CidadeDelete.as_view()), name='cidade-remove'),
    path('create', login_required(CidadeCreate.as_view()), name='cadastra-cidade'),
    path('update/<int:pk>/', login_required(CidadeUpdate.as_view()), name='edita-cidade'),
]
