
from django.shortcuts import render,get_object_or_404
from django.views.generic import DetailView,ListView
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Post, Comment
from mixin.mixins import StaffRequiredMixin
from django.views.generic.edit import CreateView,UpdateView,DeleteView
from .forms import CommentPost, PostForm
from django.urls import reverse, reverse_lazy
from django.http import JsonResponse
from django.contrib import messages


# Create your views here.

# def inicio (request):
#     post = Post.objects.all() 
#     ctx = {
#         "post" : post
#     }

#     return render (request, 'inicio.html', ctx)


class Inicio(ListView):
    model = Post
    template_name: 'inicio.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['post'] = Post.objects.all()
        return context
    

class CrearPost(LoginRequiredMixin,StaffRequiredMixin,CreateView):
    model = Post
    form_class = PostForm
    template_name = "CrearPost.html"
    success_url: '/inicio/'

    def form_valid(self, form):
        f = form.save(commit=False)
        f.author_id = self.request.user.id
        return super(CrearPost,self).form_valid(form)

    def get_form_kwargs(self):
        kwargs=super(CrearPost, self).get_form_kwargs()  
        kwargs["usuario_id"]=self.request.user.id
        return kwargs




# class BlogDetail(DetailView):
#     model = Post
#     template_name: 'details.html'


#     def get_context_data(self, **kwargs):
#         return super().get_context_data(**kwargs)

    
def post_detail(request,pk):
    template_name = 'details.html'
    post = get_object_or_404(Post, pk=pk)
    comments = post.post_comentario.all()
    new_comment = None

    

    if request.method == 'POST':
        form = CommentPost(request.POST)
        if form.is_valid():
            new_comment = form.save(commit=False)
            new_comment.post = post
            new_comment.save()
    else:
        form = CommentPost()

    return render(request, template_name, {'post': post,
                                           'comments': comments,
                                           'new_comment': new_comment,
                                           'comment_form': form,
                                           })


    



class PostUpdate(StaffRequiredMixin,UpdateView):
    model = Post
    fields = ['title','content','category']


    def get_absolute_url(self):
        
        
        
        return reverse('inicio')
    
    # def form_valid(self, form):
    #     pk = self.kwargs.get('pk')
    #     obj = get_object_or_404(Post, pk=pk)


class PostDelete(DeleteView,LoginRequiredMixin,StaffRequiredMixin):
    model = Post
    success_url = 'inicio'
    





