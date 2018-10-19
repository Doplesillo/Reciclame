from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=None,related_name='userpoints')
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

class Premio(models.Model):
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=255)
    image = models.ImageField(upload_to='images/')
    reward_points = models.IntegerField(default=0)
    pub_date = models.DateTimeField(auto_now_add=True)
    stock = models.IntegerField(default=0)

    def __str__(self):
        return self.title
