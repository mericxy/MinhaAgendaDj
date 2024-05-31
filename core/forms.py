from django import forms
from .models import Tarefa

class TarefaForm(forms.ModelForm):
    class Meta:
        model = Tarefa
        fields = ['nome', 'categoria']
        widgets = {
            'nome': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Nome',
                'style': 'background-color: #fff;',  # Define a cor de fundo e a cor do texto
            }),
            'categoria': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Categoria',
                'style': 'background-color: #fff;',  # Define a cor de fundo e a cor do texto
            }),
        }
        error_messages = {
            'nome': {
                'required': '',
            },
            'categoria': {
                'required': '',
            },
        }

