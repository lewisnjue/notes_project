from rest_framework import serializers 
from django.contrib.auth.models import User 
from .models import Notes 

class CreateUser(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username','password']
        