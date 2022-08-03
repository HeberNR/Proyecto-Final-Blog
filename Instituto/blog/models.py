from django.db import models
from django.utils import timezone
from usuario.models import Usuario

# Create your models here.


# class Category(models.Model):
#     name = models.CharField(max_length=200)

#     def __str__(self):
#         return f"{self.name}"

class Post(models.Model):
    title = models.CharField(max_length=200)
    timestamp = models.DateTimeField(default = timezone.now)
    content = models.TextField()
    # images = models.ManyToManyField('Images',upload_to = 'media', blank = True)
    # state = models.BooleanField(default = False)
    #category = models.ManyToManyField(Category, null=True, blank= True)
    description = models.CharField(max_length=200)
    author = models.ForeignKey(Usuario, on_delete=models.CASCADE, related_name = 'post')

    def __str__(self):
        return f"{self.title}"  
    

    class Meta:
        ordering = ['-timestamp']  #Ordena las publicaciones de la mas nueva a la mas antigua


# class Images(models.Models):

#     image = models.ImageField(upload_to= 'media', null = True, blank = True)