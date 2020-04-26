from django.shortcuts import render, redirect
from .forms import RegisterForm,VoterForm
from django.contrib import messages

from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm

# Create your views here.
def register(response):
    if response.method == "POST":
        #user_form = RegisterForm(response.POST)
        voter_form = VoterForm(response.POST)
        if voter_form.is_valid():
            voter_form.save()
            #messages.success(request, _('Your info was successfully saved!  We\'ll contact you soon!'))
            #return redirect('settings:profile')
        return redirect("/home") 
    else:
        #user_form = RegisterForm()
        voter_form = VoterForm()
    return render(response, "register/register.html", {
        #'user_form':user_form, 
        'voter_form':voter_form})