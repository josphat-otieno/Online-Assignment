# from django.db import models
# from django.contrib.auth.models import User
# from quizes.models import Quiz
# # Create your models here.

# class Teacher(models.Model):
#     teacher_name = models.CharField(max_length=120)
#     user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='teacher')

# class Question(models.Model):
#     text = models.CharField(max_length=100, default='')
#     quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE,)
#     # created = models.DateTimeField()

#     def __str__(self):
#         return str(self.text)

#     def get_answers(self):
#         return self.answer_set.all()


# class Answer(models.Model):
#     text = models.CharField(max_length=120, default='')
#     correct = models.BooleanField(default=False)
#     question = models.ForeignKey(Question, on_delete=models.CASCADE)
    
#     def __str__(self):
#         return f"question: {self.question.text}, answer: {self.text}, correct: {self.correct}"