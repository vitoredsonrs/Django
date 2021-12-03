from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, DeleteView, CreateView, UpdateView
from cadastros.forms import CidadeForm
from cadastros.models import Cidade


class CidadesBaseView(ListView):
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = 'Cidades'
        return context


class CidadeList(CidadesBaseView):
    queryset = Cidade.objects.all().order_by('nome')
    context_object_name = 'cidades'
    template_name = 'cadastros/lista_cidades.html'


class CidadeDetail(DetailView):
    context_object_name = 'cidade'
    queryset = Cidade.objects.all()
    template_name = 'cadastros/detalhe_cidades.html'


class CidadeDelete(DeleteView, SuccessMessageMixin):
    context_object_name = 'cidade'
    model = Cidade
    template_name = 'cadastros/remove_cidades.html'
    success_url = reverse_lazy('cidades-list')
    success_message = 'Registro deletado com sucesso!'


class CidadeCreate(CreateView):
    model = Cidade
    form_class = CidadeForm
    template_name = 'cadastros/cadastra_cidades.html'
    success_url = reverse_lazy('cidades-list')
    success_message = 'Cidade adicionada com sucesso!'


class CidadeUpdate(UpdateView, SuccessMessageMixin):
    model = Cidade
    form_class = CidadeForm
    template_name = 'cadastros/edita_cidades.html'
    success_url = reverse_lazy('cidades-list')
    success_message = 'Cadastro atualizado com sucesso!'

    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     context['titulo'] = 'Cidades'
    #     return context


# class CidadeList(View):
#
#     def get(self, request):
#         qs = Cidade.objects.all().order_by('nome')
#         context = {
#             'cidades': qs,
#             'titulo': 'Cidades'
#         }
#         return render(request, 'cadastros/lista_cidades.html', context)

    # def post(self, request):
    #     pass

#
# def lista_cidades(request):
#     qs = Cidade.objects.all().order_by('nome')
#     context = {
#         'cidades': qs,
#     }
#     return render(request, 'cadastros/lista_cidades.html', context)


# def detalhe_cidade(request, id):
#     cidade = get_object_or_404(Cidade, pk=id)
#     context = {
#         'cidade': cidade
#     }
#     return render(request, 'cadastros/detalhe_cidades.html', context)


# @login_required
# def remove_cidade(request, id):
#     cidade = get_object_or_404(Cidade, pk=id)
#     cidade.delete()
#     return redirect('cidades-list')


# @login_required
# def cadastra_cidade(request):
#     if request.method == 'POST':
#         form = CidadeForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect('cidades-list')
#     else:
#         form = CidadeForm()
#     context = {
#         'form': form
#     }
#     return render(request, 'cadastros/cadastra_cidades.html', context)
#

# @login_required
# def editar_cidade(request, id):
#     cidade_obj = get_object_or_404(Cidade, pk=id)
#     if request.method == 'GET':
#         form = CidadeForm(instance=cidade_obj)
#     else:
#         form = CidadeForm( request.POST, instance=cidade_obj)
#         if form.is_valid():
#             form.save()
#     context = {
#         'form': form,
#         'obj': cidade_obj
#     }
#     return render(request, 'cadastros/edita_cidades.html', context)

