from django.contrib import admin
from .models import *
# Register your models here.
admin.site.register(UserProfile)
admin.site.register(Punto)
admin.site.register(Residuo)
admin.site.register(Centro)
admin.site.register(LimitWaste)
admin.site.register(Premio)
admin.site.register(ResiduoLugar)
admin.site.register(Cita)