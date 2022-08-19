from dataclasses import field
import django_filters

from .models import Post

class Filter(django_filters.FilterSet):
    
    class Meta: 
        model = Post
        fields = {'category': ['exact']}