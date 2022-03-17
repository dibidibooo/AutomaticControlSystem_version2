from django import forms


# class MultipleForm(forms.ModelForm):
#     class Meta:
#         fields = ('action', )
#         widgets = ('action': )


class MultipleForm(forms.Form):
    action = forms.CharField(max_length=60, widget=forms.HiddenInput())


class Site1Form(MultipleForm):
    oil_prod = forms.CharField(max_length=50, widget=forms.TextInput, label="Нефтепродукт")
    suspended_subst = forms.CharField(max_length=50, widget=forms.TextInput, label="Взешенные вещества")
    ph = forms.CharField(max_length=50, widget=forms.TextInput, label="pH")
    oxygen_chem = forms.CharField(max_length=50, widget=forms.TextInput, label="Химическая потребность в кислороде (ХПК)")
    active_subst = forms.CharField(max_length=50, widget=forms.TextInput, label="Поверхностно-активные вещества  (АПАВ)")
    ammonium = forms.CharField(max_length=50, widget=forms.TextInput, label="Аммонийный азот")


class Site2Form(MultipleForm):
    oil_prod = forms.CharField(max_length=50, widget=forms.TextInput)
    suspended_subst = forms.CharField(max_length=50, widget=forms.TextInput)
    ph = forms.CharField(max_length=50, widget=forms.TextInput)
    oxygen_chem = forms.CharField(max_length=50, widget=forms.TextInput)
    active_subst = forms.CharField(max_length=50, widget=forms.TextInput)
    ammonium = forms.CharField(max_length=50, widget=forms.TextInput)
    oxygen_bio = forms.CharField(max_length=50, widget=forms.TextInput)
    phenols = forms.CharField(max_length=50, widget=forms.TextInput)
    chlorides = forms.CharField(max_length=50, widget=forms.TextInput)
    sulfates = forms.CharField(max_length=50, widget=forms.TextInput)
    iron = forms.CharField(max_length=50, widget=forms.TextInput)
    nitrate = forms.CharField(max_length=50, widget=forms.TextInput)
    nitrite = forms.CharField(max_length=50, widget=forms.TextInput)


# class Site3Form(MultipleForm):
#     alkalinity = forms.IntegerField(widget=forms.IntegerField)
#     hardness = forms.IntegerField(widget=forms.IntegerField)
#     oxidability = forms.IntegerField(widget=forms.IntegerField)
#     salt = forms.IntegerField(widget=forms.IntegerField)
#     chlorine = forms.IntegerField(widget=forms.IntegerField)
#
#
# class Site4Form(MultipleForm):
#     oil_prod = forms.IntegerField(widget=forms.IntegerField)
#     suspended_solids = forms.IntegerField(widget=forms.IntegerField)
#     ph = forms.IntegerField(widget=forms.IntegerField)
#     phosphorus = forms.IntegerField(widget=forms.IntegerField)
#     alkalinity = forms.IntegerField(widget=forms.IntegerField)
#     hardness = forms.IntegerField(widget=forms.IntegerField)
#     salt = forms.IntegerField(widget=forms.IntegerField)
#     chlorides = forms.IntegerField(widget=forms.IntegerField)
#     sulfates = forms.IntegerField(widget=forms.IntegerField)
#     iron = forms.IntegerField(widget=forms.IntegerField)
#     hardness_calcium = forms.IntegerField(widget=forms.IntegerField)
#     hardness_magnesium = forms.IntegerField(widget=forms.IntegerField)


# class ResultForm(forms.ModelForm):
#     class Meta:
#         model = Result
#         fields = ('component', 'value', )
#
#
# class SampleForm(forms.ModelForm):
#     class Meta:
#         model = Sample
#         fields = ('sampling_site', 'result', )
