from django import forms
# from projectapp.models import Proj
from django.contrib.auth.models import User
# from django.contrib.auth.forms import UserCreationForm
from django_recaptcha.fields import ReCaptchaField

class proj(forms.ModelForm):
    password=forms.CharField(max_length=200,widget=forms.PasswordInput)
    class Meta:
        model=User
        fields=["username", "email","password"]
    captcha=ReCaptchaField()