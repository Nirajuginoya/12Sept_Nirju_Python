from django import forms
from .models import *

class signupForm(forms.ModelForm):
    class Meta:
        models=usersignup
        fields='__all__'