from django.urls import path 
from . import views 

urlpatterns = [
    path('register',views.createuserview,name='register')
]