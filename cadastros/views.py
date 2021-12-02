from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect
from cadastros.forms import CidadeForm
from cadastros.models import Cidade


def lista_cidades(request):
    qs = Cidade.objects.all().order_by('nome')
    context = {
        'cidades': qs,
    }
    return render(request, 'cadastros/lista_cidades.html', context)


def detalhe_cidade(request, id):
    cidade = get_object_or_404(Cidade, pk=id)
    context = {
        'cidade': cidade
    }
    return render(request, 'cadastros/detalhe_cidades.html', context)


@login_required
def remove_cidade(request, id):
    cidade = get_object_or_404(Cidade, pk=id)
    cidade.delete()
    return redirect('cidades-list')


@login_required
def cadastra_cidade(request):
    if request.method == 'POST':
        form = CidadeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('cidades-list')
    else:
        form = CidadeForm()
    context = {
        'form': form
    }
    return render(request, 'cadastros/cadastra_cidades.html', context)


@login_required
def editar_cidade(request, id):
    cidade_obj = get_object_or_404(Cidade, pk=id)
    if request.method == 'GET':
        form = CidadeForm(instance=cidade_obj)
    else:
        form = CidadeForm( request.POST, instance=cidade_obj)
        if form.is_valid():
            form.save()
    context = {
        'form': form,
        'obj': cidade_obj
    }
    return render(request, 'cadastros/edita_cidades.html', context)

