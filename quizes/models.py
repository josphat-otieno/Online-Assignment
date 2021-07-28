from django.db import models
from django.contrib.auth.models import User

# Create your models here.



class Student(models.Model):
    admin_number = models.IntegerField()
    student_name = models.CharField(max_length=120)
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='student')

class Teacher(models.Model):
    teacher_name = models.CharField(max_length=120)
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='teacher')

DIFF_CHOICES =(
    ('easy,', 'easy'),
    ('medium', 'medium'),
    ('hard', 'hard'),
)

class Quiz(models.Model):
    name = models.CharField(max_length=120)
    topic = models.CharField(max_length=120)
    number_of_questions = models.IntegerField(default=1)
    time = models.IntegerField(help_text="durations of the quiz in minutes")
    required_score_to_pass = models.IntegerField(help_text="score in %")
    difficulty = models.CharField(max_length=10, choices=DIFF_CHOICES)

    def __str__(self):
        return f"{self.name}--{self.topic}"

    def get_questions(self):
        return self.question_set.all()[:self.number_of_questions]

    class Meta:
        verbose_name_plural = 'Quizes'

class Question(models.Model):
    text = models.CharField(max_length=100, default='')
    quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE,)
    created = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return str(self.text)

    def get_answers(self):
        return self.answer_set.all()

class Answer(models.Model):
    text = models.CharField(max_length=120, default='')
    correct = models.BooleanField(default=False)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    
    def __str__(self):
        return f"question: {self.question.text}, answer: {self.text}, correct: {self.correct}"

  
class Result(models.Model):
    quiz= models.ForeignKey(Quiz, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    score = models.FloatField()

    def __str__(self):
        return str(self.pk)







