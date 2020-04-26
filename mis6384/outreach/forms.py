from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from captcha.fields import ReCaptchaField
from captcha.widgets import ReCaptchaV3

class FormWithCaptcha(forms.Form):
    captcha = ReCaptchaField()

class RegisterForm(UserCreationForm):
    email = forms.EmailField()
    captcha = ReCaptchaField(widget=ReCaptchaV3)
    class Meta:
        model = User
        fields = ["username", "email", "password1", "password2"]