from django.contrib import admin
from .models import *
# Register your models here.


@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('username', 'first_name', 'last_name', 'email', 'rol')
    list_filter = ('rol',)
    search_fields = ('username', 'email', 'first_name','last_name')


admin.site.register(Punto)


@admin.register(Residuo)
class ResiduoAdmin(admin.ModelAdmin):
    list_display = ('id', 'waste_name', 'points')
    list_filter = ('waste_name','points')
    search_fields = ('waste_name',)


@admin.register(Centro)
class CentroAdmin(admin.ModelAdmin):
    list_display = ('place_name', 'place_email')
    search_fields = ('place_name',)

admin.site.register(LimitWaste)


@admin.register(Premio)
class PremioAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'description','image')
    search_fields = ('title',)


admin.site.register(ResiduoLugar)
admin.site.register(Cita)
admin.site.register(HistorialCanje)


@admin.register(Partners)
class PartnersAdmin(admin.ModelAdmin):
    list_display = ('id', 'nombre', 'direccion','telefono','email')
    search_fields = ('nombre','direccion','telefono')


admin.site.site_header = 'Reciclamex Admin'