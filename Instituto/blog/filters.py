
from django_filters import *

from .models import Post

class Filter(FilterSet):

    timestamp = DateFromToRangeFilter()
    empty_label = None
    class Meta: 
        model = Post
        fields = {'category': ['exact']}
        