from django.urls import path
from . import views

app_name = 'webpage'
urlpatterns = [
    path('', views.index, name='index'),
    path('nosotros', views.nosotros, name='nosotros'),
    path('agendar', views.agendar, name='agendar'),
    path('partners', views.partners, name='partners'),
    path('registro', views.registro, name='registro'),
    path('registro-centro', views.registroCentro, name='registro-centro'),
    path('login', views.login, name='login'),
    path('catalogo', views.catalogo, name='catalogo'),
    path('perfil', views.perfil, name='perfil'),
    path('logout', views.logout, name='logout'),
    path('citas', views.citas, name='citas'),
    path('centro', views.centro, name='centro'),
    path('cancelarcita/<int:id>', views.cancelarcita, name='cancelarcita'),
]
