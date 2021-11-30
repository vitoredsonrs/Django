from django.shortcuts import render, get_object_or_404

# Create your views here.
from cadastros.models import Cidade


def lista_cidades(request):
    # Retornar a lista de cidades cadastradas;
    # orm do Django;
    qs = Cidade.objects.all()

    context = {
        'cidades': qs,
        'titulo': 'city'
    }
    return render(request, 'cadastros/lista_cidades.html', context)


def detalhe_cidade(request):
    pass
    id_cidade = request.get['id_cidade']
    cidade = Cidade.objects.get(pk=id_cidade)

    context = {
        'cidade': detalhe_cidade()
    }

    return render(request, 'cadastros/detalhe_cidade.html', context)