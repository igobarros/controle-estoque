from django import forms
from .models import Estoque, EstoqueItens


class EstoqueForm(forms.ModelForm):

	class Meta:

		model = Estoque
		fields = ('modified', 'nf',)

class EstoqueItensForm(forms.ModelForm):

	class Meta:

		model = EstoqueItens
		fields = '__all__'