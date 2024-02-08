from django import forms
from . models import Todo
from django.forms import TextInput

class TodoForm(forms.ModelForm):
    class Meta:
        model=Todo
        fields=['title']
        widgets = {
            'title':TextInput(attrs={
                'type':"text",
                'class':"form-control",
                'placeholder':"Enter your Todo",
                'name':"title"
            })
        }