from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import Usuario



class CreateUser(UserCreationForm):
    email = forms.EmailField ()
    password1 = forms.CharField(label='Contraseña', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Confirma Contraseña', widget=forms.PasswordInput)

 
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