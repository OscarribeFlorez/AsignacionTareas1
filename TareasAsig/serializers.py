from rest_framework import serializers
from .models import Tareas, Rol

class TareaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tareas
        fields = '__all__'

class RolSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rol
        fields = '__all__'
