from django.shortcuts import render
from rest_framework import generics
from .models import Tareas, Rol
from .serializers import TareaSerializer, RolSerializer

class TareaLista(generics.ListCreateAPIView):
    queryset = Tareas.objects.all()
    serializer_class = TareaSerializer

class TareaDetalle(generics.RetrieveUpdateDestroyAPIView):
    queryset = Tareas.objects.all()
    serializer_class = TareaSerializer

class RolLista(generics.ListCreateAPIView):
    queryset = Rol.objects.all()
    serializer_class = RolSerializer

class RolDetalle(generics.RetrieveUpdateDestroyAPIView):
    queryset = Rol.objects.all()
    serializer_class = RolSerializer

# Create your views here.
