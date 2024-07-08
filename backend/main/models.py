from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Notes(models.Model):
    author = models.ForeignKey(User,on_delete=models.CASCADE,related_name='notes')
    title = models.CharField(max_length=20)
    content = models.TextField()
    