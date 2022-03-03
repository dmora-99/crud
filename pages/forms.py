from logging import PlaceHolder
from tkinter import Widget
from django import forms
from .models import Page

class PageForm(forms.ModelForm):
     
     class Meta:
         model = Page
         fields = ['title','content','order']
         widgets = {
             'title': forms.TextInput(attrs={'class':'form-control','PlaceHolder':'titulo'}),
             'content': forms.Textarea(attrs={'class':'form-control'}),
             'order': forms.NumberInput(attrs={'class':'form-control','PlaceHolder':'orden'}),
         }
