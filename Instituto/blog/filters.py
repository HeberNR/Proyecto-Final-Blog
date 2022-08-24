
from django_filters import *

from .models import Post

class Filter(FilterSet):

    timestamp = DateRangeFilter()
    class Meta: 
        model = Post
        fields = {'category': ['exact']}
        