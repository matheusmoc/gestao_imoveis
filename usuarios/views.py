from django.shortcuts import render
from django.http import HttpResponse
from rolepermissions.decorators import has_permission_decorator
from .models import Users
from django.shortcuts import redirect
from django.urls import reverse #transforma a url em nome da url
from django.contrib import auth

# Create your views here.
@has_permission_decorator('cadastrar_vendedor')
def cadastrar_vendedor(request):
    if request.method == "GET":
        return render(request, 'cadastrar_vendedor.html')
    if request.method == "POST":
        email = request.POST.get('email')
        senha = request.POST.get('senha')

        user = Users.objects.filter(email=email)
        if user.exists():
            return HttpResponse('Email já existente')
        
        #sempre usar create_user ou invés de create
        user = Users.objects.create_user(username=email, email=email, password=senha, cargo="V")

        return HttpResponse('Conta criada')

def login(request):
    if request.method == "GET":
        if request.user.is_authenticated:
            return redirect(reverse('dashboard'))
        return render(request, 'login.html')
    elif request.method == "POST":
        login = request.POST.get('email')
        senha = request.POST.get('senha')

        print(login, senha)

        user = auth.authenticate(username=login, password=senha)
        if not user:
            return HttpResponse('Usuário inválido')
        auth.login(request, user)
        return HttpResponse('Usuário logado')

def logout(request):
    request.session.flush()
    return redirect(reverse('login'))