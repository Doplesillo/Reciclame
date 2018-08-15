from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def index(request):
    return render(request, 'webpage/index.html')

def nosotros(request):
    return render(request, 'webpage/nosotros.html')

def agendar(request):
    return render(request, 'webpage/agendar.html')

def partners(request):
    return render(request, 'webpage/partners.html')

def registro(request):
    return render(request, 'webpage/registro.html')

def login(request):
    return render(request, 'webpage/login.html')


