from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=None)
    total_points = models.IntegerField(default=0)

    def __str__(self):
        return '%s %s %s' % (self.user.first_name, self.user.last_name, self.total_points)

class Residuo(models.Model):
    waste_name =models.CharField(max_length=100)
    points = models.IntegerField(default=0)

    def __str__(self):
        return self.waste_name

class centro(models.Model):
    place_name = models.CharField(max_length=100)
    place_email = models.CharField(max_length=100)

    def __str__(self):
        return self.place_name


class Punto(models.Model):
    user = models.ForeignKey(UserProfile,on_delete=models.CASCADE)
    waste = models.ForeignKey(Residuo, on_delete=models.CASCADE)

    def __str__(self):
        return '%s %s' % (self.user, self.waste)

class LimitWaste(models.Model):
    place = models.ForeignKey(centro, on_delete=models.CASCADE)
    waste = models.ForeignKey(Residuo, on_delete=models.CASCADE)
    limit = models.IntegerField(default=0)

    def __str__(self):
        return '%s %s limite: %s' % (self.place,self.waste,self.limit)