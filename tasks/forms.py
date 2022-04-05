from django import forms

from projects.models import TaskAssign


class TaskUpdateForm(forms.ModelForm):
    class Meta:
        model = TaskAssign
        fields = ('deadline', 'user', 'status',)
