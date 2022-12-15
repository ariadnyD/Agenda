from django import forms as django_forms
from django.contrib.auth import forms
from django.contrib.auth.models import User
from django.forms import ModelForm
from myapp.models import *

class UserCreationForm(forms.UserCreationForm):
    first_name = django_forms.CharField(max_length=150, label="Nome", required=False)
    username = django_forms.EmailField(max_length=150, label="E-mail", required=True)
    class Meta:
        model = User
        fields = ["first_name", "username", "password1", "password2"]

    def __init__(self, *args, **kwargs):
        super(UserCreationForm, self).__init__(*args, **kwargs)

        for fieldname in ['username', 'password1', 'password2']:
            self.fields[fieldname].help_text = None

class TarefaForm(ModelForm):
    class Meta:
        model = Tarefa 
        fields = ["nome", "descricao", "dataConclusao", "status", "materia"]

class MateriaForm(ModelForm):
    class Meta:
        model = Materia 
        fields = ["nome"]

class StatusForm(ModelForm):
    class Meta:
        model = Status_das_tarefas 
        fields = ["nome"]