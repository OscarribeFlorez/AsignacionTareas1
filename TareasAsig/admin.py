from django.contrib import admin
from .models import Tareas, Rol, PerfilUsuario
# Register your models here.
admin.site.register(Tareas)
admin.site.register(Rol)
admin.site.register(PerfilUsuario)