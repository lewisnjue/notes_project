from django.shortcuts import render
from .serializers import CreateUser 
from rest_framework.response import Response 
from rest_framework.decorators import api_view
from rest_framework.permissions import IsAuthenticated

# Create your views here.
@api_view(['POST'])
def createuserview(request):
    user = CreateUser(data=request.data)
    user.is_valid(raise_exception=True)
    user.save()
    return Response({'message':'user created successfuly'})


