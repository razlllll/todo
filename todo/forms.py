from django import forms
from .models import Todo
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class TodoForm(forms.ModelForm):
    class Meta:
        model = Todo
        fields = ['title', 'description', 'due_date']
        widgets = {
            'due_date': forms.DateInput(attrs={'type': 'date'})
        }
