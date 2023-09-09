from django.db import models
from django.contrib.auth.models import User

class Rol(models.Model):
    nombre = models.CharField(max_length=50)
    def __str__(self):
        return self.nombre
        
class Tareas(models.Model):
     Tipo_tarea = (
        ('Tarea', 'Tarea'),
        ('trabajo', 'Trabajo'),
        ('evalucion', 'Evaluacion'),
     )

     Estado = (
        ('proceso', 'Proceso'),
        ('Pendiente', 'Pendiente'),
        ('terminada', 'Terminada'),
     )

 
     titulo= models.CharField(max_length=200)
     tipo = models.CharField(max_length=15, choices=Tipo_tarea)
     descripccion = models.TextField(blank=True)
     Estado= models.CharField(max_length=15, choices=Estado)
     asignada_a = models.ManyToManyField(User, related_name='tareas_asignadas', blank=True)
     def __str__(self):
        return self.titulo
    
class PerfilUsuario(models.Model):
    usuario = models.OneToOneField(User, on_delete=models.CASCADE)
    rol = models.ForeignKey(Rol, on_delete=models.SET_NULL, null=True)
    # Otros campos del perfil de usuario, si es necesario.
    def __str__(self):
        return self.usuario, self.rol
        







# Create your models here.
