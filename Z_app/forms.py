from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.forms import ModelForm
from Z_app.models import User, Product


class LoginForm(forms.Form):
    login = forms.CharField(max_length=64)
    password = forms.CharField(max_length=64, widget=forms.PasswordInput, label="Hasło")


class MyUserCreationForm(UserCreationForm):

    class Meta(UserCreationForm.Meta):
        model = User
        fields = ('username', 'email', 'password1', 'password2', 'type', 'profile_image')
