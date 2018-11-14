from django.shortcuts import render, redirect
from django.core.mail import send_mail
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib import auth
from .models import *
from django.contrib.auth.decorators import login_required


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


@login_required(login_url="/login")
def agendar(request):
    user = UserProfile.objects.get(pk=request.session['id'])
    lugares = Centro.objects.all()
    residuos = Residuo.objects.all()
    limite = LimitWaste.objects.all()
    if user is not None:
        if user.rol == '1':
            if request.method == 'POST':
                cita = Cita()
                cita.lugar = Centro.objects.get(pk=request.POST['lugar'])
                cita.fecha_cita = request.POST['fecha']
                cita.residuo = Residuo.objects.get(pk=request.POST['residuo'])
                cita.num_residuos = request.POST['cantidad']
                cita.user = UserProfile.objects.get(pk=request.session['id'])
                cita.save()
                return render(request, 'webpage/agendar.html',
                              {'success': 'Tu cita a sido Agendada exitosamente', 'lugares': lugares,
                               'residuos': residuos, 'limite': limite})
            else:
                return render(request, 'webpage/agendar.html',
                              {'lugares': lugares, 'residuos': residuos, 'limite': limite})
        elif user.rol == '2':
            return redirect('webpage:centro')
        elif user.rol == '3':
            return redirect('admin/')
    else:
        return render(request, 'webpage/index.html')


def partners(request):
    return render(request, 'webpage/partners.html')


def registro(request):
    #TODO
    if user is not None:
        if request.method == 'POST':
            if User.objects.filter(username=request.POST['username']).exists():
                return render(request, 'webpage/registro.html', {'error': 'Usuario ya registrado'})
            elif User.objects.filter(email=request.POST['email']).exists():
                return render(request, 'webpage/registro.html', {'error': 'Email ya registrado'})
            else:
                # usuario no esta en database y quiere una cuenta nueva
                if request.POST['pass'] == request.POST['pass2']:
                    if request.POST['email'] == request.POST['email2']:
                        user = User.objects.create_user(request.POST['username'],
                                                        email=request.POST['email'],
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
    else:
        return redirect('webpage:index')


def login(request):
    if request.method == 'POST':
        user = auth.authenticate(username=request.POST['username'], password=request.POST['pass'])
        if user is not None:
            usuario = UserProfile.objects.get(username=request.POST['username'])
            auth.login(request, user)
            print(usuario.rol)
            request.session['username'] = usuario.username
            request.session['rol'] = usuario.rol
            request.session['id'] = usuario.pk
            if usuario.rol == '1':
                return redirect('webpage:index')
            elif usuario.rol == '2':
                return redirect('webpage:partners')
            elif usuario.rol == '3':
                return redirect('webpage:nosotros')
            else:
                return render(request, 'webpage/login.html',
                              {'error': 'la cuenta no tiene rol, habla con el administrador'})
        else:
            return render(request, 'webpage/login.html', {'error': 'username or password is incorrect'})
    else:
        return render(request, 'webpage/login.html')


def logout(request):
    if request.method == 'POST':
        auth.logout(request)
        return redirect('webpage:index')


def catalogo(request):
    premio = Premio.objects.order_by('-pub_date')
    return render(request, 'webpage/catalogo.html', {'premios': premio})


@login_required(login_url="/login")
def perfil(request):
    user = UserProfile.objects.get(pk=request.session['id'])
    articulos = Punto.objects.filter(user=request.session['id']).all()
    if user is not None:
        if user.rol == '1':
            for numero in articulos:
                numeros = numero.cantidad * numero.waste.points
            # print(articulos)
            puntos = 0
            for articulo in articulos:
                puntos = articulo.cantidad * articulo.waste.points + puntos
                # print(articulo)
                # print(puntos)
            # print("===============")
            # print(puntos)
            return render(request, 'webpage/perfil.html', {'user': user, 'articulos': articulos, 'puntos': puntos})
        elif user.rol == '2':
            return redirect('webpage:centro')
        elif user.rol == '3':
            return redirect('admin/')
    else:
        return redirect('webpage:index')


@login_required(login_url="/login")
def citas(request):
    cita = Cita.objects.filter(user=request.session['id']).all()
    user = UserProfile.objects.get(pk=request.session['id'])
    if user is not None:
        if user.rol == '1':
            return render(request, 'webpage/citas.html', {'user': user, 'cita': cita})
        elif user.rol == '2':
            return redirect('webpage:centro')
        elif user.rol == '3':
            return redirect('admin/')
    else:
        return redirect('webpage:index')


@login_required(login_url="/login")
def centro(request):
    user = UserProfile.objects.get(pk=request.session['id'])
    if user is not None:
        if user.rol == '1':
            return render(request, 'webpage/index.html')
        elif user.rol == '2':
            return render(request, 'webpage/centro.html', {'user': user})
        elif user.rol == '3':
            return render(request, 'webpage/index.html')
    else:
        return render(request, 'webpage/index.html')
