from django.shortcuts import render

# Create your views here.
from cadastros.models import Cidade


def lista_cidades(request):
    # Retornar a lista de cidades cadastradas;
    # orm do Django;
    qs = Cidade.objects.all()
    qs_capital = Cidade.objects.filter(capital=True)



