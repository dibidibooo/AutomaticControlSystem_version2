from crispy_forms.helper import FormHelper
from allauth.account.forms import LoginForm,SignupForm,ChangePasswordForm,ResetPasswordForm,ResetPasswordKeyForm,SetPasswordForm
from django.contrib.auth.forms import AuthenticationForm
from django import forms


class UserLoginForm(LoginForm):
    def __init__(self, *args, **kwargs):
        super(UserLoginForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper(self)
        self.fields['login'].widget = forms.TextInput(attrs={'class': 'form-control mb-2','placeholder':'Введите имя пользователя','id':'username'})
        self.fields['password'].widget = forms.PasswordInput(attrs={'class': 'form-control mb-2','placeholder':'Введите пароль','id':'password'})
        self.fields['remember'].widget = forms.CheckboxInput(attrs={'class': 'form-check-input'})
        self.fields['login'].label="<b>Имя пользователя</b>"
        self.fields['password'].label="<b>Пароль</b>"
class UserRegistrationForm(SignupForm):
    def __init__(self, *args, **kwargs):
        super(UserRegistrationForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper(self)
        self.fields['email'].widget = forms.EmailInput(attrs={'class': 'form-control mb-1','placeholder':'Enter Email','id':'email'})
        self.fields['email'].label="Email"
        self.fields['username'].widget = forms.TextInput(attrs={'class': 'form-control mb-1','placeholder':'Введите имя пользователя','id':'username1'})
        self.fields['password1'].widget = forms.PasswordInput(attrs={'class': 'form-control mb-1','placeholder':'Введите пароль','id':'password1'})
        self.fields['password2'].widget = forms.PasswordInput(attrs={'class': 'form-control mb-1','placeholder':'Повторите пароль','id':'password2'})
        self.fields['password2'].label="<b>Подтвердите пароль</b>"
class PasswordChangeForm(ChangePasswordForm):
      def __init__(self, *args, **kwargs):
        super(PasswordChangeForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper(self)

        self.fields['oldpassword'].widget = forms.PasswordInput(attrs={'class': 'form-control mb-2','placeholder':'Введите текущий пароль','id':'password3'})
        self.fields['password1'].widget = forms.PasswordInput(attrs={'class': 'form-control mb-2','placeholder':'Введите новый пароль','id':'password4'})
        self.fields['password2'].widget = forms.PasswordInput(attrs={'class': 'form-control mb-2','placeholder':'Повторите пароль','id':'password5'})
        self.fields['oldpassword'].label="<b>Текущий пароль</b>"
        self.fields['password1'].label="<b>Новый пароль</b>"
        self.fields['password2'].label="<b>Подтвердите пароль</b>"
class PasswordResetForm(ResetPasswordForm):
      def __init__(self, *args, **kwargs):
        super(PasswordResetForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper(self)

        self.fields['email'].widget = forms.EmailInput(attrs={'class': 'form-control mb-2','placeholder':'Введите Email','id':'email1'})
        self.fields['email'].label="Email"
class PasswordResetKeyForm(ResetPasswordKeyForm):
      def __init__(self, *args, **kwargs):
        super(PasswordResetKeyForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper(self)
        self.fields['password1'].widget = forms.PasswordInput(attrs={'class': 'form-control mb-2','placeholder':'Введите новый пароль','id':'password6'})
        self.fields['password2'].widget = forms.PasswordInput(attrs={'class': 'form-control mb-1','placeholder':'Повторите пароль','id':'password7'})
        self.fields['password2'].label="<b>Подтвердите пароль</b>"
class PasswordSetForm(SetPasswordForm):
      def __init__(self, *args, **kwargs):
        super(PasswordSetForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper(self)
        self.fields['password1'].widget = forms.PasswordInput(attrs={'class': 'form-control mb-2','placeholder':'Введите новый пароль','id':'password8'})
        self.fields['password2'].widget = forms.PasswordInput(attrs={'class': 'form-control','placeholder':'Повторите пароль','id':'password9'})
        self.fields['password2'].label="<b>Подтвердите пароль</b>"