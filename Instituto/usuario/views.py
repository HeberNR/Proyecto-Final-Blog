from django.shortcuts import render
from django.views.generic.edit import CreateView
from .forms import CreateUser
from .models import Usuario
from django.urls import reverse
# Create your views here.



class Registro(CreateView):
    model = Usuario
    form_class = CreateUser
    template_name = "registro.html"

    def get_success_url(self, **kwargs):
        return reverse('inicio')