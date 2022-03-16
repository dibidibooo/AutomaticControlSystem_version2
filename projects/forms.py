from django import forms

from .models import Result, Sample


class ResultForm(forms.ModelForm):
    class Meta:
        model = Result
        fields = ('component', 'value', )


class SampleForm(forms.ModelForm):
    class Meta:
        model = Sample
        fields = ('sampling_site', 'result', )
