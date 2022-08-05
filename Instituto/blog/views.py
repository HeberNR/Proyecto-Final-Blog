from django.shortcuts import render
<<<<<<< HEAD
from .models import Post
from django.views.generic import TemplateView
=======
from .models import Post, Comment
>>>>>>> 07c4b453435d7e0047f188f140864ccdd4188ea9
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


# class BlogDetail(TemplateView):
#     model: Post
#     template_name: "details.html"


    
#     def get_context_data(self, **kwargs):
#         context = super(Comment, self).get_context_data(**kwargs)
#         return context
    



class CrearComentario(CreateView):
    model = Comment
    form_class = CommentPost
    template_name = "Comentario.html"

    def get_success_url(self, **kwargs):
        return reverse ("inicio")
