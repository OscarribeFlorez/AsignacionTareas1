from django.urls import path
from .views import TareaLista, TareaDetalle, RolLista, RolDetalle

urlpatterns = [
    path('tareas/', TareaLista.as_view(), name='tarea-lista'),
    path('tareas/<int:pk>/', TareaDetalle.as_view, name='tarea-detalle'),
    path('roles/', RolLista.as_view, name='rol-lista'),
    path('roles/<int:pk>/', RolDetalle.as_view, name='rol-detalle'),
]
