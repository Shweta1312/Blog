from django import forms
from django.contrib.auth.models import User
from .models import *

class UserForm(forms.ModelForm):
    
    class Meta:
        model=Profile
        fields=['phone','age','bio','interests','image']

  