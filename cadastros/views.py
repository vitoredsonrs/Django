from django.shortcuts import render, get_object_or_404

# Create your views here.
from cadastros.models import Cidade


def lista_cidades(request):
    # Retornar a lista de cidades cadastradas;
    # orm do Django;
    qs = Cidade.objects.all()

    context = {
        'cidades': qs,
    }
    return render(request, 'cadastros/lista_cidades.html', context)


def detalhe_cidade(request, id):

    # id_cidade = 9
    # cidade = Cidade.objects.get(pk=id_cidade)
    cidade = get_object_or_404(Cidade, pk=id)

    context = {
        'cidade': cidade
    }

    return render(request, 'cadastros/detalhe_cidades.html', context)
