from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from captcha.fields import ReCaptchaField
from captcha.widgets import ReCaptchaV3
from dobwidget import DateOfBirthWidget
from outreach.models import Voter

class FormWithCaptcha(forms.Form):
    captcha = ReCaptchaField()

class RegisterForm(UserCreationForm):
    email = forms.EmailField()
    #birthdate = forms.DateField()
    captcha = ReCaptchaField(widget=ReCaptchaV3)
    class Meta:
        model = User
        fields = ["username",  ]


class VoterForm(forms.ModelForm):
    class Meta:
        model = Voter
        fields = ("email", "first_name", "last_name", 'phone','date_of_birth', 'address', 'city', 'state', 'zipcode')
        widgets = {'date_of_birth': DateOfBirthWidget(),
            }