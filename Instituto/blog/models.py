from distutils.command.upload import upload
from xml.etree.ElementInclude import include
from django.db import models
from django.utils import timezone
from usuario.models import Usuario
from django.urls import reverse




class Category(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return f"{self.name}"

class Post(models.Model):
    title = models.CharField(max_length=200)
    timestamp = models.DateTimeField(auto_now_add=True)
    content = models.TextField()
    image = models.ImageField(upload_to= 'uploads_post', null = True, blank = True)
    # slug = models.SlugField(unique=True,null=False)
    # state = models.BooleanField(default = False)
    category = models.ForeignKey(Category, null=True,on_delete=models.DO_NOTHING, blank= False,related_name='categoria_post') #cambiar blank a "False"
    description = models.CharField(max_length=200)
    author = models.ForeignKey(Usuario, on_delete=models.CASCADE, related_name = 'post')

    def __str__(self):
        return f"{self.title}"  
    
    # def save(self, *args, **kwargs):
    #     if not self.slug:
    #         self.slug = slugify(self.title)
    #         super().save(*args, **kwargs)

    def get_absolute_url(self):
        
        return reverse('inicio')



    class Meta:
        ordering = ['-timestamp']  #Ordena las publicaciones de la mas nueva a la mas antigua

class Comment(models.Model):
    content = models.TextField()
    timestamp = models.DateTimeField(default = timezone.now)
    author = models.ForeignKey(Usuario, on_delete=models.CASCADE, related_name = 'autor_commentario')
    posts = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')

    def __str__(self):
        return f"{self.content}"



class Archivos(models.Model):
    nombre = models.CharField(max_length=200)
    archivo = models.FileField(upload_to = 'archivos' )

    def __str__(self):
        return f"{self.nombre}"