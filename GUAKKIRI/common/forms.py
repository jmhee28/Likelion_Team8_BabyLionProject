from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import UserChangeForm
from django.contrib.auth import get_user_model
from MainApp.models import User
from django.contrib.auth.forms import ReadOnlyPasswordHashField

class UserForm(UserCreationForm):
    email = forms.EmailField(label="email")
    major = forms.CharField(label = "major")
    university = forms.CharField(label = "university")
    class Meta:
        model = User
        fields = ("university", "major","username", "email", "address", "phone_number")

class CustomUserChangeForm(forms.ModelForm):
    password = None
    class Meta:
        model =  User
        fields = ("university", "major","username", "email", "address", "phone_number")