from django import forms
from .models import Todolist, Userlist

class TodoAdd(forms.ModelForm):
    class Meta:
        model = Todolist
        fields = ['day','content']
        
        widgets = {
            'day': forms.NumberInput(attrs={
                "type": "date"
            })
        }


class UserAdd(forms.ModelForm):
    class Meta:
        model = Userlist
        fields = ['name','password']