from django import forms
from django.db.models import fields
from .models import *

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
         fields = ['']

class QuizForm(forms.ModelForm):
    class Meta:
        model = Quiz

class AnswerForm(forms.ModelForm):
    class Meta:
        model = Answer





# class ProfileUpdateForm(forms.ModelForm)
#     class Meta:
#         model = UserProfile
#         fields = ['bio', 'profile_photo', 'phone_number']






