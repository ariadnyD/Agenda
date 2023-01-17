from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from myapp.forms import *
from django.contrib.auth import authenticate, login
from django.contrib import messages
from myapp.models import *
from datetime import date, timedelta

def permissao(request):
    if request.user.is_authenticated:
        return True
    return False

def permissao2(request, obj):
    if request.user.is_authenticated:
        if obj.usuario == request.user:
            return True
    return False

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
    if permissao(request) == False:
        return redirect('/login')

    mate = Materia.objects.filter(usuario = request.user)
    search = request.GET.get('search')

    data_atual = date.today()
    afazerTd = Tarefa.objects.filter(status = "AFA").filter(usuario = request.user).order_by('dataConclusao')
    andamentoTd = Tarefa.objects.filter(status = "AND").filter(usuario = request.user).order_by('dataConclusao')
    finalizada = Tarefa.objects.filter(status = "FIN").filter(usuario = request.user).order_by('dataConclusao')
    atrasadas_afazer = []
    atrasadas_andamento = []
    afazer = []
    andamento = []
    if search:
        afazerTd = afazerTd.filter(nome__icontains=search)
        andamentoTd = andamentoTd.filter(nome__icontains=search)
        finalizada = finalizada.filter(nome__icontains=search)
    for i in afazerTd:
        if i.dataConclusao < data_atual:
            atrasadas_afazer.append(i)
        else:
            afazer.append(i)
    for i in andamentoTd:
        if i.dataConclusao < data_atual:
            atrasadas_andamento.append(i)
        else:
            andamento.append(i)

    data_atual_alert = date.today()
    tarefas_user = Tarefa.objects.filter(usuario = request.user)
    tarefa_alerta = []
    dt = data_atual_alert + timedelta(hours=24)
    for i in tarefas_user:
        if i.dataConclusao == dt:
            tarefa_alerta.append(i)
    pacote = {
        "afa": afazer,
        "and": andamento,
        "fin": finalizada,
        "atra_afa": atrasadas_afazer,
        "atra_and": atrasadas_andamento,
        "materias": mate,
        "alertas": tarefa_alerta
    }
    return render(request, "inicio.html", pacote)

def formTarefa(request):
    if permissao(request) == False:
        return redirect('/login')
    mate = Materia.objects.filter(usuario = request.user)
    if request.method == "POST":
        formTarefa = TarefaForm(request.POST, request.FILES)
        if formTarefa.is_valid():
            obj = Tarefa.objects.create(
                nome = formTarefa.cleaned_data.get("nome"),
                usuario = request.user,
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
    pacote = {"formTarefa": formTarefa, "materias": mate}
    return render(request, "formTarefa.html", pacote)

def updateTarefa(request, id):
    if permissao2(request, Tarefa.objects.get(pk = id)) == False:
        return redirect('/login')
    mate = Materia.objects.filter(usuario = request.user)
    update =True
    tarefaid = Tarefa.objects.get(pk=id)
    formTarefa = TarefaModelForm(request.POST or None, request.FILES or None, instance=tarefaid)
    if formTarefa.is_valid():
        formTarefa.save()
        return redirect("/inicio")
    pacote = {"formTarefa": formTarefa, "update": update, "materias": mate}
    return render(request, "formTarefa.html", pacote)

def detTarefa(request, id):
    if permissao2(request, Tarefa.objects.get(pk = id)) == False:
        return redirect('/login')
    mate = Materia.objects.filter(usuario = request.user)
    tarefaid = Tarefa.objects.get(pk=id)
    pacote = {"tarefa": tarefaid, "materias": mate}
    return render(request, "detTarefa.html", pacote)

def deleteTarefa(request, id):
    if permissao2(request, Tarefa.objects.get(pk = id)) == False:
        return redirect('/login')
    tarefaid = Tarefa.objects.get(pk=id)
    tarefaid.delete()
    return redirect("/inicio")

def showMateria(request):
    if permissao(request) == False:
        return redirect('/login')
    mate = Materia.objects.filter(usuario = request.user)
    pacote = {"materias": mate}
    return render(request, "materia.html", pacote)

def formMateria(request):
    if permissao(request) == False:
        return redirect('/login')
    mate = Materia.objects.filter(usuario = request.user)
    formMateria = MateriaForm(request.POST or None)
    if request.method == "POST":
        formMateria = MateriaForm(request.POST or None)
        if formMateria.is_valid():
            obj = Materia.objects.create(
                nome = formMateria.cleaned_data.get("nome"),
                usuario = request.user,
                horario = formMateria.cleaned_data.get("horario"),
            )
            obj.save()
            return redirect("/showMateria")
    pacote = {"formMateria": formMateria, "materias": mate}
    return render(request, "formMateria.html", pacote)

def deleteMateria(request, id):
    if permissao2(request, Materia.objects.get(pk = id)) == False:
        return redirect('/login')
    materiaid = Materia.objects.get(pk=id)
    materiaid.delete()
    return redirect("/showMateria")

def layout(request):
    return render(request, 'layouts/agenda.html')

def pMateria(request, id):
    if permissao(request) == False:
        return redirect('/login')
    mate = Materia.objects.filter(usuario = request.user)
    data_atual = date.today()
    afazerTd = Tarefa.objects.filter(status = "AFA").filter(materia = Materia.objects.get(pk = id)).filter(usuario = request.user).order_by('dataConclusao')
    andamentoTd = Tarefa.objects.filter(status = "AND").filter(materia = Materia.objects.get(pk = id)).filter(usuario = request.user).order_by('dataConclusao')
    finalizada = Tarefa.objects.filter(status = "FIN").filter(materia = Materia.objects.get(pk = id)).filter(usuario = request.user).order_by('dataConclusao')
    atrasadas_afazer = []
    atrasadas_andamento = []
    afazer = []
    andamento = []
    for i in afazerTd:
        if i.dataConclusao < data_atual:
            atrasadas_afazer.append(i)
        else:
            afazer.append(i)
    for i in andamentoTd:
        if i.dataConclusao < data_atual:
            atrasadas_andamento.append(i)
        else:
            andamento.append(i)
    
    pacote = {
        "afa": afazer,
        "and": andamento,
        "fin": finalizada,
        "atra_afa": atrasadas_afazer,
        "atra_and": atrasadas_andamento,
        "materias": mate,
    }
    return render(request, "inicio.html", pacote)