from django.shortcuts import render, redirect
from django.core.mail import send_mail
from django.conf import settings
from django.template.loader import get_template
from django.contrib import auth
from .models import *
from django.contrib.auth.decorators import login_required
import datetime



# Create your views here.
def index(request):
    return render(request, 'webpage/index.html')


def nosotros(request):
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
                send_mail('Hello from Reciclame',  # subject
                          'Tienes una cita el dia'+ ' ' + str(cita.fecha_cita) + ' ' + 'en' + ' ' + str(cita.lugar) + ' ' + 'te esperamos',  # body
                          'jmanuel.chairez@cucea.udg.mx',  # domain email
                          ['manuelchairezudg@gmail.com'],  # email that recieve
                          fail_silently=True  # show if fails
                          )
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
    if request.method == 'POST':
        if UserProfile.objects.filter(username=request.POST['username']).exists():
            return render(request, 'webpage/registro.html', {'error': 'Usuario ya registrado'})
        elif UserProfile.objects.filter(email=request.POST['email']).exists():
            return render(request, 'webpage/registro.html', {'error': 'Email ya registrado'})
        else:
            # usuario no esta en database y quiere una cuenta nueva
            if request.POST['pass'] == request.POST['pass2']:
                if request.POST['email'] == request.POST['email2']:
                    user = UserProfile.objects.create_user(request.POST['username'],
                                                           email=request.POST['email'],
                                                           password=request.POST['pass'],
                                                           rol='1')
                    user.first_name = request.POST['name']
                    user.last_name = request.POST['lastname']
                    user.save()
                    usuario = UserProfile.objects.get(username=request.POST['username'])
                    request.session['username'] = usuario.username
                    request.session['rol'] = usuario.rol
                    request.session['id'] = usuario.pk
                    auth.login(request, user)
                    return redirect('webpage:index')
                else:
                    return render(request, 'webpage/registro.html', {'error': 'Los emails no son iguales'})
            else:
                return render(request, 'webpage/registro.html', {'error': 'Las contraseñas no son Iguales'})
    else:
        return render(request, 'webpage/registro.html')


def registroCentro(request):
    try:
        user = UserProfile.objects.get(pk=request.session['id'])
    except:
        print('Entre ala exception')
        return redirect('webpage:index')
    if user is not None:
        if user.rol == '1':
            return redirect('webpage:index')
        elif user.rol == '2':
            return redirect('webpage:index')
        elif user.rol == '3':
            if request.method == 'POST':
                if UserProfile.objects.filter(username=request.POST['username']).exists():
                    return render(request, 'webpage/registro-centro.html', {'error': 'Usuario ya registrado'})
                elif UserProfile.objects.filter(email=request.POST['email']).exists():
                    return render(request, 'webpage/registro-centro.html', {'error': 'Email ya registrado'})
                else:
                    # usuario no esta en database y quiere una cuenta nueva
                    if request.POST['pass'] == request.POST['pass2']:
                        if request.POST['email'] == request.POST['email2']:
                            user = UserProfile.objects.create_user(request.POST['username'],
                                                                   email=request.POST['email'],
                                                                   password=request.POST['pass'],
                                                                   rol='2')
                            user.save()
                            return render(request, 'webpage/registro-centro.html',
                                          {'exito': 'Registro Exitoso'})
                        else:
                            return render(request, 'webpage/registro-centro.html',
                                          {'error': 'Los emails no son iguales'})
                    else:
                        return render(request, 'webpage/registro-centro.html',
                                      {'error': 'Las contraseñas no son Iguales'})
            else:
                return render(request, 'webpage/registro-centro.html')
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
                return redirect('webpage:centro')
            elif usuario.rol == '3':
                return redirect('webpage:index')
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
    usuario = UserProfile.objects.get(id=request.session['id'])
    premio = Premio.objects.order_by('-pub_date')
    if request.method == 'POST':
        premio_canje = Premio.objects.get(pk=request.POST['premio_id'])
        if usuario.puntos_totales < premio_canje.reward_points:
            msg = 'No tienes suficientes puntos para canjearlo'
            return render(request, 'webpage/catalogo.html', {'premios': premio, 'msg': msg})
        usuario.puntos_totales = usuario.puntos_totales - premio_canje.reward_points
        usuario.save()
        return redirect('webpage:perfil')
    return render(request, 'webpage/catalogo.html', {'premios': premio})


@login_required(login_url="/login")
def perfil(request):
    user = UserProfile.objects.get(pk=request.session['id'])
    articulos = Cita.objects.filter(user__cita=request.session['id'], user__cita__Estatus=1).all()
    if user is not None:
        if user.rol == '1':
            for numero in articulos:
                numeros = numero.num_residuos * numero.residuo.points
             #print(articulos)
            puntos = 0
            for articulo in articulos:
                puntos = articulo.num_residuos * articulo.residuo.points + puntos
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


def canje(request):
    if request.method == 'POST':
        premio = Premio.objects.get(pk=request.POST['id'])
        usuario = UserProfile.objects.get(username=request.session['id'])
        usuario.puntos_totales = usuario.puntos_totales - premio.reward_points
        usuario.save()
    return redirect('webpage:perfil')


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


def cancelarcita(request, id):
    cita = Cita.objects.get(pk=id)
    cita.Estatus = 1
    cita.save()
    return redirect('webpage:citas')

@login_required(login_url="/login")
def centro(request):
    user = UserProfile.objects.get(pk=request.session['id'])
    cita = Cita.objects.all()
    if user is not None:
        if user.rol == '1':
            return render(request, 'webpage/index.html')
        elif user.rol == '2':
            return render(request, 'webpage/centro.html', {'user': user, 'cita': cita})
        elif user.rol == '3':
            return render(request, 'webpage/index.html')
    else:
        return render(request, 'webpage/index.html')
