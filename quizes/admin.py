from django.contrib import admin
from .models import *

# Register your models here.
class AnswerInline(admin.TabularInline):
    model = Answer
    extra = 3

class QuestionAdmin(admin.ModelAdmin):
    inlines = [AnswerInline]

admin.site.register(Question, QuestionAdmin)
admin.site.register(Answer)
admin.site.register(Teacher)
admin.site.register(Quiz)
admin.site.register(Result)
admin.site.register(Student)

