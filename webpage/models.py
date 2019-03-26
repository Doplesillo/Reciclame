from django.db import models

from django.contrib.auth.models import AbstractUser
import datetime
from django.utils import timezone

# Create your models here.
class UserProfile(AbstractUser):
    ROLES =(
        ('1','Usuario'),
        ('2', 'Centro'),
        ('3', 'Admin'),
    )
    rol = models.CharField(max_length=3, choices=ROLES)
    puntos_totales = models.IntegerField(default=0)




#Admin, Controlara los residuos disponibles para que no puedan levantar los centros cualquier residuo
class Residuo(models.Model):
    waste_name =models.CharField(max_length=100)
    points = models.IntegerField(default=0)

    def __str__(self):
        return self.waste_name

#Admin, nomnbre de los centros de reciclaje disponibles
class Centro(models.Model):
    place_name = models.CharField(max_length=100)
    place_email = models.CharField(max_length=100)

    def __str__(self):
        return self.place_name

#El centro asigna los residuos que puede tener, siempre y cuando solo sea los dados de alta
class ResiduoLugar(models.Model):
    lugar = models.ForeignKey(Centro, on_delete=models.CASCADE)
    residuo = models.ForeignKey(Residuo, on_delete=models.CASCADE)
    limite = models.IntegerField()

    def __str__(self):
        return '%s - %s' % (self.lugar.place_name, self.residuo.waste_name)


class Punto(models.Model):
    user = models.ForeignKey(UserProfile,on_delete=models.CASCADE)
    waste = models.ForeignKey(Residuo, on_delete=models.CASCADE)
    cantidad = models.IntegerField()
    total = models.IntegerField()


    def __str__(self):
        return '%s %s' % (self.user, self.waste)

class LimitWaste(models.Model):
    place = models.ForeignKey(Centro, on_delete=models.CASCADE)
    waste = models.ForeignKey(Residuo, on_delete=models.CASCADE)
    limit = models.IntegerField(default=0)

    def __str__(self):
        return '%s %s limite: %s' % (self.place,self.waste,self.limit)


class Premio(models.Model):
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=255)
    image = models.ImageField(upload_to='static/webpage/images/catalogo/')
    reward_points = models.IntegerField(default=0)
    pub_date = models.DateTimeField(auto_now_add=True)
    stock = models.IntegerField(default=0)

    def __str__(self):
        return self.title

class Cita(models.Model):
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE,default=1)
    lugar = models.ForeignKey(Centro, on_delete=models.CASCADE)
    residuo = models.ForeignKey(Residuo, on_delete=models.CASCADE)
    fecha_cita = models.DateField(auto_now=False)
    num_residuos = models.IntegerField(default=1)
    fecha_aprobacion = models.DateField(default=None, blank=True, null=True)
    Estatus = models.IntegerField(default=0)

    def __str__(self):
        return str(self.fecha_cita)


class HistorialCanje(models.Model):
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    fecha = models.DateField()
    articulo = models.CharField(max_length=40)
    antes = models.IntegerField(default=0)
    despues = models.IntegerField(default=0)


class Partners(models.Model):
    nombre = models.CharField(max_length=50, default="Pendiente")
    descripcion = models.CharField(max_length=50, default=" ")
    direccion = models.CharField(max_length=100, default=" ")
    telefono = models.IntegerField(default=0)
    horario = models.CharField(max_length=25, default=" ")
    email = models.CharField(max_length=50, default=" ")
    pagina = models.CharField(max_length=80, default=" ")
    giro = models.CharField(max_length=40, default=" ")
    image = models.ImageField(upload_to='static/webpage/images/partners/', default="example.jpg")

    def __str__(self):
        return self.nombre






