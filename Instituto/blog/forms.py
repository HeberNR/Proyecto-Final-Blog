from django import forms
from .models import Archivos, Post, Comment

class PostForm(forms.ModelForm):
    
    
    class Meta : 
        model=Post
        fields= ["title",'image', "content", "description",'category']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', }),
            
            'content': forms.Textarea(attrs={'class': 'form-control content', }),
            'description': forms.TextInput(attrs={'class': 'form-control', }),
            'category': forms.Select(attrs={'class': 'form-control', }),

        } 
        labels = {
            'title': 'Titulo',
            'image': 'Imagen',
            'content': 'Contenido',
            'description': 'Descripción',
            'category': 'Categoría',
        }
    
    def __init__(self, usuario_id, *args, **kwargs):
        super(PostForm, self).__init__(*args, **kwargs)
        


class CommentPost(forms.ModelForm):
    class Meta : 
        model=Comment
        fields= ["content"]
        widgets = {
            'content': forms.Textarea(attrs={'class': 'form-control', }),
        }
    
    def __init__(self, *args, **kwargs):
        super(CommentPost, self).__init__(*args, **kwargs)
        self.fields['content'].label = ""



class UploadFile(forms.ModelForm):
    class Meta : 
        model=Archivos
        fields= ["nombre","archivo"]
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control', }),
            'archivo': forms.FileInput(attrs={'class': 'form-control', })
        }