from django import forms

from tickets.models import Solicitacao


class NovaSolicitacaoForm(forms.ModelForm):

    class Meta:
        model = Solicitacao
        fields = ['categoria', 'nome', 'email', 'assunto', 'descricao', 'arquivo']