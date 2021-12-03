from django import forms
from cadastros.models import Cidade


class CidadeForm(forms.ModelForm):
    class Meta:
        model = Cidade
        fields = '__all__'
