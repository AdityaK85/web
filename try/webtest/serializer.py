from .models import *
from rest_framework import serializers
from rest_framework.serializers import (
      ModelSerializer,
)


class studentSerializer(serializers.ModelSerializer):
    class Meta:
        model = testmod
        fields = '__all__'

# Image Upload Serializer 
class imageSerializer(ModelSerializer):
   class Meta:
      model = login
      fields = [
        'username',
        'email',
        'profile_pic'        
      ]