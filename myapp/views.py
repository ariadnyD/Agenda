from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from myapp.forms import *
from django.contrib.auth import authenticate, login
from django.contrib import messages
from myapp.models import *

def login_user(request):
    if request.user.is_authenticated:
        return redirect('/inicio')
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect("/inicio")
        else:
            messages.success(request, ("E-mail ou senha inválidos"))
    return render(request, "login.html")

def sair(request):
    request.session.flush()
    return redirect('/login')

def cadastro(request):
    formUsuario = UserCreationForm()
    if request.method == "POST":
        formUsuario = UserCreationForm(request.POST)
        if formUsuario.is_valid():
            obj = User.objects.create(
                first_name = formUsuario.cleaned_data.get("first_name"),
                username = formUsuario.cleaned_data.get("username"),
            )
            obj.set_password(formUsuario.cleaned_data["password1"])
            obj.save()
            
            return redirect("/login")
    else:
        formUsuario = UserCreationForm()
    pacote = {"formUsuario": formUsuario}
    return render(request, "cadastro.html", pacote)

def index(request):
    return render(request, "index.html")

def inicio(request):
    afazer = Tarefa.objects.filter(status = "AFA").order_by('dataConclusao')
    andamento = Tarefa.objects.filter(status = "AND").order_by('dataConclusao')
    finalizada = Tarefa.objects.filter(status = "FIN").order_by('dataConclusao')
    pacote = {
        "afa": afazer,
        "and": andamento,
        "fin": finalizada,
    }
    return render(request, "inicio.html", pacote)

def formTarefa(request):
    if request.method == "POST":
        formTarefa = TarefaForm(request.POST, request.FILES)
        if formTarefa.is_valid():
            obj = Tarefa.objects.create(
                nome = formTarefa.cleaned_data.get("nome"),
                descricao = formTarefa.cleaned_data.get("descricao"),
                dataConclusao = formTarefa.cleaned_data.get("dataConclusao"),
                status = formTarefa.cleaned_data.get("status"),
                materia = formTarefa.cleaned_data.get("materia"),
                arquivo = formTarefa.cleaned_data.get("arquivo"),
            )
            obj.save()
            return redirect("/inicio")
    else:
        formTarefa = TarefaForm()
    pacote = {"formTarefa": formTarefa}
    return render(request, "formTarefa.html", pacote)

def updateTarefa(request, id):
    update =True
    tarefaid = Tarefa.objects.get(pk=id)
    formTarefa = TarefaModelForm(request.POST or None, request.FILES or None, instance=tarefaid)
    if formTarefa.is_valid():
        formTarefa.save()
        return redirect("/inicio")
    pacote = {"formTarefa": formTarefa, "update": update}
    return render(request, "formTarefa.html", pacote)

def detTarefa(request, id):
    tarefaid = Tarefa.objects.get(pk=id)
    pacote = {"tarefa": tarefaid}
    return render(request, "detTarefa.html", pacote)

def deleteTarefa(request, id):
    tarefaid = Tarefa.objects.get(pk=id)
    tarefaid.delete()
    return redirect("/inicio")

def showMateria(request):
    materias = Materia.objects.all()
    pacote = {"materias": materias}
    return render(request, "materia.html", pacote)

def formMateria(request):
    formMateria = MateriaForm(request.POST or None)
    if formMateria.is_valid():
        formMateria.save()
        return redirect("/showMateria")
    pacote = {"formMateria": formMateria}
    return render(request, "formMateria.html", pacote)

def deleteMateria(request, id):
    materiaid = Materia.objects.get(pk=id)
    materiaid.delete()
    return redirect("/showMateria")

def layout(request):
    return render(request, 'layouts/agenda.html')
