from django import forms


class MultipleForm(forms.Form):
    action = forms.CharField(max_length=60, widget=forms.HiddenInput())


class Site1Form(MultipleForm):
    oil_prod = forms.CharField(max_length=50, widget=forms.TextInput(attrs={'class': 'form-control'}), label="Нефтепродукт")
    suspended_subst = forms.CharField(max_length=50, widget=forms.TextInput(attrs={'class': 'form-control'}), label="Взвешенные вещества")
    ph = forms.CharField(max_length=50, widget=forms.TextInput(attrs={'class': 'form-control'}), label="pH")
    oxygen_chem = forms.CharField(max_length=50, widget=forms.TextInput(attrs={'class': 'form-control'}), label="Химическая потребность в кислороде (ХПК)")
    active_subst = forms.CharField(max_length=50, widget=forms.TextInput(attrs={'class': 'form-control'}), label="Поверхностно-активные вещества  (АПАВ)")
    ammonium = forms.CharField(max_length=50, widget=forms.TextInput(attrs={'class': 'form-control'}), label="Аммонийный азот")


class Site2Form(MultipleForm):
    oil_prod = forms.CharField(max_length=50, widget=forms.TextInput(attrs={'class': 'form-control'}),
                               label="Нефтепродукт")
    suspended_subst = forms.CharField(max_length=50, widget=forms.TextInput(attrs={'class': 'form-control'}),
                                      label="Взвешенные вещества")
    ph = forms.CharField(max_length=50, widget=forms.TextInput(attrs={'class': 'form-control'}), label="pH")
    oxygen_chem = forms.CharField(max_length=50, widget=forms.TextInput(attrs={'class': 'form-control'}),
                                  label="Химическая потребность в кислороде (ХПК)")
    active_subst = forms.CharField(max_length=50, widget=forms.TextInput(attrs={'class': 'form-control'}),
                                   label="Поверхностно-активные вещества  (АПАВ)")
    ammonium = forms.CharField(max_length=50, widget=forms.TextInput(attrs={'class': 'form-control'}),
                               label="Аммонийный азот")
    oxygen_bio = forms.CharField(max_length=50, widget=forms.TextInput(attrs={'class': 'form-control'}),
                               label="Биологическая потребность в кислороде (БПК5)")
    phenols = forms.CharField(max_length=50, widget=forms.TextInput(attrs={'class': 'form-control'}),
                               label="Фенолы")
    chlorides = forms.CharField(max_length=50, widget=forms.TextInput(attrs={'class': 'form-control'}),
                               label="Хлориды")
    sulfates = forms.CharField(max_length=50, widget=forms.TextInput(attrs={'class': 'form-control'}),
                               label="Сульфаты")
    iron = forms.CharField(max_length=50, widget=forms.TextInput(attrs={'class': 'form-control'}),
                               label="Железо")
    nitrate = forms.CharField(max_length=50, widget=forms.TextInput(attrs={'class': 'form-control'}),
                               label="Азот нитратов")
    nitrite = forms.CharField(max_length=50, widget=forms.TextInput(attrs={'class': 'form-control'}),
                               label="Азот нитритов")


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

