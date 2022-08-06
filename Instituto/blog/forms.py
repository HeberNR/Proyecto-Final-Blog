from django import forms
from .models import Post, Comment

class PostForm(forms.ModelForm):
    
    
    class Meta : 
        model=Post
        fields= ["title",'image', "content", "description",'category']
    
    def __init__(self, usuario_id, *args, **kwargs):
        super(PostForm, self).__init__(*args, **kwargs)


class CommentPost(forms.ModelForm):
    class Meta : 
        model=Comment
        fields= ["posts","content"]
        widgets = {            
            "content": forms.Textarea(attrs={"class": "form-control"})
        }

