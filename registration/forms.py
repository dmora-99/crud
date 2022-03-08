from dataclasses import fields
import email
from msilib.schema import Class
from pyexpat import model
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class UserCreationFormWithEmail (UserCreationForm):
    email = forms.EmailField(required=True,help_text="Campo Obligatorio")

    class Meta:
        model = User
        fields = ("username","email","password1","password2")

