from django.contrib import admin
from django.contrib.admin.options import TabularInline
from django.db import models
from .models import Teacher, Question,Quiz
from student.models import Answer
# Register your models here.

admin.site.register(Teacher)

# admin.site.register(Quiz)

class AnswerInline(admin.TabularInline):
    model = Answer

class QuestionAdmin(admin.ModelAdmin):
    inlines = [AnswerInline]

admin.site.register(Question, QuestionAdmin)