from django import forms
from .models import Day, Todo


class TaskForm(forms.ModelForm):
        class Meta:
            model = Todo
            fields = ['task', 'last']
