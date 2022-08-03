from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import Usuario



class CreateUser(UserCreationForm):

 
    class Meta:
        model = Usuario
        fields = ['first_name','last_name','username','email']
        help_texts = {k: "" for k in fields}

        labels = {

            'username': 'Nombre de usuario',
            'first_name': 'Nombre',
            'last_name': 'Apellido',
            'email': 'Correo',

        }