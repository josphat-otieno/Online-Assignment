from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Teacher(models.Model):
    teacher_name = models.CharField(max_length=120)
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='teacher')

class Quiz(models.Model):
    pass

class Question(models.Model):
    pass

