from django import forms
from django.contrib.auth.forms import UserChreationForm
from django.contrib.auth.models import User

class SignuoForm(UserChreationForm):
    class  Meta:
        model=User
        fields=['username','email','password1','password2']
        
class UserActivateForm(forms.Form):
    code=forms.ChoiceField(max_length=10)