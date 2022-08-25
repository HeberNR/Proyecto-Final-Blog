
from pipes import Template
from django.shortcuts import render,get_object_or_404,redirect
from django.views.generic import DetailView,ListView,TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Post, Comment
from core.mixins import StaffRequiredMixin
from django.views.generic.edit import CreateView,UpdateView,DeleteView
from .forms import CommentPost, PostForm
from django.urls import reverse, reverse_lazy
from .filters import Filter



class Inicio(ListView):
    model = Post
    template_name= 'inicio.html'
    paginate_by: 2

    def get_queryset(self):
        queryset = super().get_queryset()
        filter = Filter(self.request.GET, queryset)
        return filter.qs
        

    def get_context_data(self, **kwargs):              
        context = super().get_context_data(**kwargs)
        context['post'] = Post.objects.all()
        context['filter'] = Filter(self.request.GET, queryset=self.get_queryset())
        return context
    

class CrearPost(LoginRequiredMixin,StaffRequiredMixin,CreateView):
    model = Post
    form_class = PostForm
    template_name = "CrearPost.html"
    success_url= '/'

    def form_valid(self, form):
        f = form.save(commit=False)
        f.author_id = self.request.user.id
        return super(CrearPost,self).form_valid(form)

    def get_form_kwargs(self):
        kwargs=super(CrearPost, self).get_form_kwargs()  
        kwargs["usuario_id"]=self.request.user.id
        return kwargs




class BlogDetail(DetailView):
    model = Post
    template_name= 'details.html'
    form = CommentPost
    def get_context_data(self, **kwargs):
        
        context = super().get_context_data(**kwargs)
        context['form'] = self.form
        context['comments'] = self.object.comments.all()
        return context


    def post(self, request, *args, **kwargs):
        form = CommentPost(request.POST)
        if form.is_valid():
            post = self.get_object()
            form.instance.author = self.request.user
            form.instance.posts = post
            form.save()
            return redirect(reverse('details', kwargs={'pk': post.id}))    
        else:
            return self.form_invalid(form)

    def get_success_url(self):
        return reverse('details', kwargs = {'pk': self.object.id})

 


class PostUpdate(StaffRequiredMixin,UpdateView):
    model = Post
    form_class= PostForm
    # fields = ['title','content','category']

    # def get_absolute_url(self):
        
    #     return reverse('inicio')
    def get_success_url(self):
        return reverse('details', kwargs = {'pk': self.object.id})
    def get_form_kwargs(self):
        kwargs=super(PostUpdate, self).get_form_kwargs()  
        kwargs["usuario_id"]=self.request.user.id
        return kwargs
    

class PostDelete(DeleteView,LoginRequiredMixin,StaffRequiredMixin):
    model = Post
    success_url = '/'
    template_name = 'details.html'
    



class Mision(TemplateView):
    template_name = 'mision.html'
    

    def get_success_url(self):
        return reverse('mision')

class Nosotros(TemplateView):
    template_name = 'quienesomos.html'
    
    def get_success_url(self):
    
        return reverse('nosotros')