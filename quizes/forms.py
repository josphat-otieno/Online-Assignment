from django import forms
from django.db.models import fields
from .models import *
from django.forms import inlineformset_factory

from django.contrib.auth.models import User
from django.contrib.auth.forms import UserChangeForm

class EditProfileForm(UserChangeForm):
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'form-control'}))
    first_name = forms.CharField(max_length=100, widget=forms.TextInput( attrs={'class': 'form-control'}))
    last_name = forms.CharField(max_length=100, widget=forms.TextInput( attrs={'class': 'form-control'}))
    username = forms.CharField(max_length=100, widget=forms.TextInput( attrs={'class': 'form-control'}))
    
    class Meta:
        model =User
        fields = ['username', 'first_name', 'last_name', 'email', ]
        

class QuestionForm(forms.ModelForm):
    class Meta:
         model = Question
         fields = ['text']

class QuizForm(forms.ModelForm):
    class Meta:
        model = Quiz
        fields = ['name', 'topic', 'number_of_questions','required_score_to_pass','time','difficulty']

class AnswerForm(forms.ModelForm):
    class Meta:
        model = Answer
        fields = ['text', 'correct']


class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ['admin_number',]

