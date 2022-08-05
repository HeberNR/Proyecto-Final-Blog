from django.shortcuts import render
from .models import Post, Comment
from django.views.generic.edit import CreateView,UpdateView
from .forms import CommentPost, PostForm
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

class CrearComentario(CreateView):
    model = Comment
    form_class = CommentPost
    template_name = "Comentario.html"

    def get_success_url(self, **kwargs):
        return reverse ("inicio")