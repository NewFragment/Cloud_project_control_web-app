from .models import *
from django.forms import ModelForm, TextInput
from django import forms


class userForm(ModelForm):
    class Meta:
        model = user
        fields = ["email", "password"]
