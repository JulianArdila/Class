from rest_framework import serializers
from .models import User
from django.contrib.auth.models import Group

class UserSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = User
        exclude = ('is_superuser','is_staff' )
        extra_kwargs = {
            'password': {'write_only': True},
            'username': {'write_only': True},
            'birthday': {'required': True},
        }
    
    def create(self, validated_data, instance=None):
        print(validated_data)
        user = User(**validated_data)
        user.set_password(validated_data['password'])
        user.save()
        kwargs = {
            'id':1
        }
        group = Group.objects.get(**kwargs)
        #kwargs['parametro_2'] = 5
        #args = (1, )
        #self.prueba(parametro_1=2, parametro_2=4,*args,**kwargs)
        #group = Group.objects.get(id=1)
        group.user_set.add(user)
        return user

    def prueba(self, parametro_1, parametro_2= 2, *args, **kwargs):
        print(parametro_1)
        print(parametro_2)
        print(args)
        print(kwargs.pop('id', None))
        pass