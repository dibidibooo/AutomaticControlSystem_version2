from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.models import User, Group
from django.core.exceptions import ValidationError


class ProfileForm(forms.ModelForm):
    first_name = forms.CharField(label="Имя", required=True)
    last_name = forms.CharField(label="Фамилия", required=True)
    email = forms.CharField(label="Почта", required=True)
    phone = forms.CharField(label="Телефон", required=True, widget=forms.TextInput(attrs={'placeholder': 'Телефон'}))
    role = forms.ModelChoiceField(label="Роль пользователя", required=True, widget=forms.Select, queryset=Group.objects.all())
    position = forms.CharField(label="Должность", required=True, widget=forms.TextInput(attrs={'placeholder': 'Должность'}))
    password1 = forms.CharField(label="Пароль", strip=False, required=True, widget=forms.PasswordInput)
    password2 = forms.CharField(label="Подтвердите пароль", required=True, widget=forms.PasswordInput,
                                strip=False)

    def clean(self):
        cleaned_data = super().clean()
        email = cleaned_data.get('email')
        password = cleaned_data.get("password1")
        password_confirm = cleaned_data.get("password2")
        if password and password_confirm and password != password_confirm:
            raise ValidationError('Пароли не совпадают!')
        if User.objects.filter(email=email).exists():
            raise ValidationError("Указанный email существует")
        return cleaned_data

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data['password1'])
        if commit:
            user.save()
        return user

    class Meta:
        model = get_user_model()
        fields = (
            'username', 'first_name', 'last_name', 'email',
            'password1', 'password2',
        )


class ProfileEditForm(forms.ModelForm):
    first_name = forms.CharField(label="Имя", widget=forms.TextInput(attrs={'id': 'first_name', 'placeholder': 'Имя'}))
    last_name = forms.CharField(label="Фамилия", widget=forms.TextInput(attrs={'id': 'last_name', 'placeholder': 'Фамилия'}))
    phone = forms.CharField(label="Телефон", widget=forms.TextInput(attrs={'id': 'phone', 'placeholder': 'Телефон'}))
    position = forms.CharField(label="Должность", widget=forms.TextInput(attrs={'id': 'position', 'placeholder': 'Должность'}))
    role = forms.ModelChoiceField(label="Роль пользователя", widget=forms.Select, queryset=Group.objects.all())

    class Meta:
        model = get_user_model()
        fields = ["first_name", "last_name", "phone", "position"]
