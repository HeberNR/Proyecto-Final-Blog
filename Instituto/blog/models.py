from django.db import models
from django.utils import timezone
from usuario.models import Usuario

# Create your models here.


class Category(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return f"{self.name}"

class Post(models.Model):
    title = models.CharField(max_length=200)
    timestamp = models.DateTimeField(default = timezone.now)
    content = models.TextField()
    image = models.ImageField(upload_to= 'uploads_post', null = True, blank = True)
    # state = models.BooleanField(default = False)
    category = models.ForeignKey(Category, null=True,on_delete=models.DO_NOTHING, blank= True,related_name='categoria_post')
    description = models.CharField(max_length=200)
    author = models.ForeignKey(Usuario, on_delete=models.CASCADE, related_name = 'post')

    def __str__(self):
        return f"{self.title}"  
    

    class Meta:
        ordering = ['-timestamp']  #Ordena las publicaciones de la mas nueva a la mas antigua


