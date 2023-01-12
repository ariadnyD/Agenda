from django import forms as django_forms
from django.contrib.auth import forms
from django.contrib.auth.models import User
from django.forms import ModelForm
from django.contrib.admin.widgets import AdminDateWidget
from myapp.models import *

class DateInput(django_forms.DateInput):
    input_type = 'date'

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

status_choice=(
    ("AFA","A fazer"),
    ("AND","Em andamento"),
    ("FIN", "Finalizada"),
)

class TarefaForm(django_forms.Form):
    nome = django_forms.CharField(max_length=100, label="Dê um nome a sua tarefa:")
    descricao = django_forms.CharField(widget=django_forms.Textarea, max_length=280, label="Descrição:")
    dataConclusao = django_forms.DateField(label="Data para conclusão da tarefa:", required=False, widget=DateInput())
    status = django_forms.ChoiceField(choices=status_choice)
    # esse select de matéria não consegui fazer pra pegar só do usuário atual
    materia = django_forms.ModelChoiceField(queryset=Materia.objects.all(), label="Matéria", required=False)
    arquivo = django_forms.FileField(label="Arquivo", required=False)

class TarefaModelForm(ModelForm):
    class Meta:
        model = Tarefa 
        fields = ["nome", "descricao", "dataConclusao", "status", "materia", "arquivo"]

        labels = {
            "nome": "Dê um nome a sua tarefa:",
            "descricao": "Descrição:",
            "dataConclusao":"Data para conclusão da tarefa:",
            "status": "Status:",
            "materia": "Matéria",
            "arquivo": "Arquivo",
        }

class MateriaForm(django_forms.Form):
    nome = django_forms.CharField(max_length=50, label="Nome da matéria:")
    horario = django_forms.CharField(max_length=50, label="Horário:")
