from django.db import models
from django.contrib.auth.models import User
from teacher.models import Question
from quizes.models import Quiz
# Create your models here.
class Student(models.Model):
    admin_number = models.IntegerField()
    name = models.CharField(max_length=120)
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='student')
    
class Result(models.Model):
    quiz= models.ForeignKey(Quiz, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    score = models.FloatField()

    def __str__(self):
        return str(self.pk)