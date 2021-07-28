from django.db import models

# Create your models here.

DIFF_CHOICES =(
    ('easy,', 'easy'),
    ('medium', 'medium'),
    ('hard', 'hard'),
)

class Quiz(models.Model):
    name = models.CharField(max_length=120)
    topic = models.CharField(max_length=120)
    number_of_questions = models.IntegerField
    time = models.IntegerField(help_text="durations of the quiz in minutes")
    requred_score_to_pass = models.IntegerField(help_text="score in %")
    difficulty = models.CharField(max_length=10, choices=DIFF_CHOICES)

    def __str__(self):
        return f"{self.name}--{self.topic}"

    def get_question(self):
        return self.question_set.all()

