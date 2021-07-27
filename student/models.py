from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Student(models.Model):
    admin_number = models.IntegerField()
    name = models.CharField(max_length=120)
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='student')
    
class Answer(models.Model):
    pass