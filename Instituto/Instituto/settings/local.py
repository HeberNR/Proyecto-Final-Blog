from .base import *

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'blogdb',
        'USER': 'root',
        'PASSWORD': 'admin12345',
        'HOST': 'localhost',
        'PORT': '3306',
        
    }
}