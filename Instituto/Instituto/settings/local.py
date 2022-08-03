from .base import *
import os
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'blogpruebas',
        'USER': 'root',
        'PASSWORD': 'admin12345',
        'HOST': 'localhost',
        'PORT': '3306',
        
    }
}

STATICFILES_DIRS = (
    os.path.join(os.path.dirname(BASE_DIR), "static"),

)
print(STATICFILES_DIRS)