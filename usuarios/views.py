from django.shortcuts import render
from django.http import HttpResponse
from rolepermissions.decorators import has_permission_decorator
from .models import Users
from django.shortcuts import redirect
from django.urls import reverse #transforma a url em nome da url
from django.contrib import auth
from django.shortcuts import get_object_or_404
from django.contrib import messages

# Create your views here.
@has_permission_decorator('cadastrar_vendedor')
def cadastrar_vendedor(request):
    if request.method == "GET":
        vendedores = Users.objects.filter(cargo="V")
        return render(request, 'cadastrar_vendedor.html', {'vendedores': vendedores})
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

@has_permission_decorator('cadastrar_vendedor')
def desativar_usuario(request, id):
    vendedor = get_object_or_404(Users, id=id)
    vendedor.is_active = False
    vendedor.save()
    messages.add_message(request, messages.SUCCESS, 'Vendedor desativado com sucesso!')
    return redirect(reverse('cadastrar_vendedor'))