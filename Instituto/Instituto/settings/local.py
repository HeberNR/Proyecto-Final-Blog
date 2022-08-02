from .base import *
import os
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'blogbd',
        'USER': 'root',
        'PASSWORD': 'Heber201222',
        'HOST': 'localhost',
        'PORT': '3306',
        
    }
}

STATICFILES_DIRS = (
    os.path.join(os.path.dirname(BASE_DIR), "static"),

)