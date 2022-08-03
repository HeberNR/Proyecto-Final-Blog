from .base import *
import os
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'blogdbprueba',
        'USER': 'root',
        'PASSWORD': 'Macfdlr4',
        'HOST': 'localhost',
        'PORT': '3306',
        
    }
}

STATICFILES_DIRS = (
    os.path.join(os.path.dirname(BASE_DIR), "static"),

)