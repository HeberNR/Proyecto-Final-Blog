from django.shortcuts import render
from .models import Post
from django.views.generic.edit import CreateView,UpdateView
from .forms import PostForm
from django.urls import reverse

# Create your views here.

def inicio (request):
    post = Post.objects.all() 
    ctx = {
        "post" : post
    }

    return render (request, 'inicio.html', ctx)


class CrearPost(CreateView):
    model = Post
    form_class = PostForm
    template_name = "CrearPost.html"

    def get_success_url(self, **kwargs):
        return reverse ("inicio")

