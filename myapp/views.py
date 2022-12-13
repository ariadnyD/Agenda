from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from myapp.forms import UserCreationForm
from django.contrib.auth import authenticate, login
from django.contrib import messages

def login_user(request):
    if request.user.is_authenticated:
        return redirect('/inicio')
    if request.method == "POST":
        print("oi")
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
    return render(request, "inicio.html")
