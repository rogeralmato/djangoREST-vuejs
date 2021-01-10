from rest_framework import serializers
from .models import Usuario
    
class UsuarioSerializer(serializers.HyperlinkedModelSerializer):
    email = serializers.EmailField(source='user.email')
    is_staff = serializers.BooleanField(source='user.is_staff')
    class Meta:
        model = Usuario
        fields = ['first_name', 'last_name', 'is_staff', 'email']