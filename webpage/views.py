from django.shortcuts import render, redirect
from django.core.mail import send_mail
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib import auth
from .models import *


# Create your views here.
def index(request):
    return render(request, 'webpage/index.html')


def nosotros(request):
    """
     send_mail('Hello from Reciclame', #subject
               'Si funciona el service provider', #body
               '', #domain email
               ['manuelchairezudg@gmail.com'], #email that recieve
               fail_silently=False # show if fails
               )
     """
    return render(request, 'webpage/nosotros.html')


def agendar(request):
    lugares = centro.objects.all()
    residuos = Residuo.objects.all()
    limite = LimitWaste.objects.all()
    return render(request, 'webpage/agendar.html', {'lugares':lugares,'residuos':residuos,'limite':limite})


def partners(request):
    return render(request, 'webpage/partners.html')


def registro(request):
    if request.method == 'POST':
        if User.objects.filter(username=request.POST['username']).exists():
            return render(request, 'webpage/registro.html', {'error': 'Usuario ya registrado'})
        elif User.objects.filter(email=request.POST['email']).exists():
            return render(request, 'webpage/registro.html', {'error': 'Email ya registrado'})
        else:
            # usuario no esta en database y quiere una cuenta nueva
            if request.POST['pass'] == request.POST['pass2']:
                if request.POST['email'] == request.POST['email2']:
                    user = User.objects.create_user(request.POST['username'], email=request.POST['email'],
                                                    password=request.POST['pass'])
                    user.first_name = request.POST['name']
                    user.last_name = request.POST['lastname']
                    user.save()
                    auth.login(request, user)
                    return redirect('webpage:index')
                else:
                    return render(request, 'webpage/registro.html', {'error': 'Los emails no son iguales'})
            else:
                return render(request, 'webpage/registro.html', {'error': 'Las contraseñas no son Iguales'})
    else:
        return render(request, 'webpage/registro.html')


def login(request):
    if request.method == 'POST':
        user = auth.authenticate(username=request.POST['username'],password=request.POST['pass'])
        if user is not None:
            auth.login(request, user)
            return redirect('webpage:index')
        else:
            return render(request, 'webpage/login.html', {'error':'username or password is incorrect'})
    else:
        return render(request, 'webpage/login.html')

def logout(request):
    if request.method == 'POST':
        auth.logout(request)
        return redirect('webpage:index')


def catalogo(request):
    return render(request, 'webpage/catalogo.html')


def perfil(request):
    return render(request, 'webpage/perfil.html')
