from rest_framework import serializers
from .models import User


class UserSerializer(serializers.ModelSerializer):


    username = serializers.CharField(write_only=True,
    source="username")
    password = serializers.CharField(write_only=True,
    source="password")
    birthday = serializers.DateField(required=True)
    
    class Meta:
        model = User
        fields = '__all__'
        
