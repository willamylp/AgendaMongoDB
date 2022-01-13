from django.contrib.auth import forms
from django.forms.models import fields_for_model
from .models import User

class UserChangeForms(forms.UserChangeForm) :
    class Meta(forms.UserChangeForm.Meta):
        model = User

class UserCreationForms(forms.UserCreationForm) :
    class Meta(forms.UserCreationForm.Meta):
        model = User
        fields= ['username','first_name','last_name','email', 'password1', 'password2']

class UserAutenticationForm(forms.AuthenticationForm):
    class Meta(forms.AuthenticationForm):
        model = User
        fields =['username','password']
