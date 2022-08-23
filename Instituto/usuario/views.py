
from django.views.generic.edit import CreateView
from .forms import CreateUser
from .models import Usuario
from django.contrib.auth import authenticate, login
from django.http import HttpResponseRedirect
from django.urls import reverse
# Create your views here.



class Registro(CreateView):
    model = Usuario
    form_class = CreateUser
    template_name = "registro.html"
    success_url= "/"

    # def get_success_url(self, **kwargs):
    #     return reverse('inicio')


