from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User #Usando as tabelas de auth_user já instanciadas pelo django
from django.contrib import messages, auth #Utilizando as mensagens
from django.contrib.messages import constants
from django.contrib.auth import authenticate, login, logout #Autentificando os usuários

def cadastro(request):
    #Fazer uma verificação para caso o usuário já esteja logado
    if request.user.is_authenticated:
        return redirect('/divulgar/novo_pet')

    if request.method == "GET": #Pela url (GET)
        return render(request,'cadastro.html')
    elif request.method == "POST": #Quando apertado o botão (POST)
        #Pegando os dados no front
        nome = request.POST.get('nome')
        email = request.POST.get('email')
        senha = request.POST.get('senha')
        confirmar_senha = request.POST.get('confirmar_senha')

        #Validações básicas de dados

        ##Usuário preencheu todos os campos
        if len(nome.strip()) == 0 or len(email.strip()) == 0 or len(senha.strip()) == 0 or len(confirmar_senha.strip()) == 0: #strip tira espaços do começo e fim
            messages.add_message(request,constants.ERROR,'Preencha todos os campos!')
            return render(request,'cadastro.html')
        
        if senha != confirmar_senha:
            messages.add_message(request,constants.ERROR,'Digite duas senhas iguais!')
            return render(request,'cadastro.html')

        #Cadastrar usuário na base de dados
        try: #O uso de tratamento de exceção se dá por conta de possíveis erros que podem ocorrer com o banco
            user = User.objects.create_user(
                username=nome,
                email=email,
                password=senha
            )
            #Mensagem de sucesso
            messages.add_message(request,constants.SUCCESS,'Usuário cadastrado com sucesso!')
            return render(request,'cadastro.html')
        except:
            #Mensagem de erro
            messages.add_message(request,constants.Warning,'O usuário não pode ser cadastrado, tente novamente!')
            return render(request,'cadastro.html')

        
def logar(request): #Nome dessa função não pode ser igual a nome de métodos
    #Fazer uma verificação para caso o usuário já esteja logado
    if request.user.is_authenticated:
        # Seria bom colocar uma tela inicial do próprio usuário
        return redirect('/divulgar/novo_pet')

    if request.method == "GET":
        return render(request,'login.html')
    elif request.method == "POST": #No clicar de login
        nome = request.POST.get('nome')
        senha = request.POST.get('senha')

        #Autenticando o usuário
        user = authenticate(username=nome,password=senha)

        if user is not None:
            #Logar
            login(request,user)
            return redirect('/divulgar/novo_pet')
        else:
            #Mensagem de erro
            messages.add_message(request,constants.WARNING,'Usuário ou senha incorretos')
            return render(request,'login.html')

def logout(request):
    auth.logout(request)
    return redirect('/auth/login')