from django import forms
from django.forms import ModelForm

from tasks.models import Comment, Task


class CommentForm(ModelForm):
    class Meta:
        model = Comment
        fields = ('text', )


class TaskForm(ModelForm):
    deadline = forms.DateTimeField(error_messages={'required': 'Это обязательное поле'})

    class Meta:
        model = Task
        fields = ('status', 'user', 'deadline', )
