from django import forms 
from django.contrib.auth.forms import UserCreationForm 
from django.contrib.auth import get_user_model 

class UserCreateForm(UserCreationForm):
    class Meta:
        model = get_user_model()
        fields = ['username', 'email', 'password1', 'password2']
        help_texts = {
            'username': None, 
            'email': None, 
            'password1': None, 
            'password2': None, 
        }