from django import forms
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.forms import ModelForm

from users.models import User


class UserRegisterForm(UserCreationForm):

    class Meta:
        model = User
        fields = (
            "first_name",
            "email",
            "password1",
            "password2",
        )


class UserForm(ModelForm):

    class Meta:
        model = User
        fields = (
            "first_name",
            "last_name",
        )
