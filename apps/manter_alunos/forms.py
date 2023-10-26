from .models import Aluno
from django.forms import ModelForm

class AlunoForm(ModelForm):
    class Meta:
        model = Aluno
        fields = ['nome', 'endereco', 'email', 'data_de_nascimento', 'curso', 'cidade']