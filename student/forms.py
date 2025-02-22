from instructor.models import User

from django.contrib.auth.forms import UserCreationForm

from django import forms

class StudentCreateForm(UserCreationForm):

    class Meta:

        model=User

        fields=["username","email","password1","password2"]

class LoginForm(forms.Form):

    username=forms.CharField()

    password=forms.CharField()