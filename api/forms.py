from django import forms
from .models import Colors
from django.utils.translation import ugettext_lazy as _

class ClorsForm(forms.ModelForm):
	class Meta:
		model=Colors
		fields='__all__'
		labels={
		'name':_('nombre'),
		'hexadecimal':_('hexadecimal'),
		'red':_('rojo'),
		'green':_('verde'),
		'blue':_('azul')
		}
		widgets = {
			'name': forms.Textarea(attrs={'placeholder': 'pon un nombre'})
		}