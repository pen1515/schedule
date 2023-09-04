from django import forms
from .models import Todolist

class TodoAdd(forms.ModelForm):
    class Meta:
        model = Todolist
        fields = ['day','content']