from .base import *

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'blogdb',
        'USER': 'root',
        'PASSWORD': '',
        'HOST': 'localhost',
        'PORT': '3306',
        
    }
}

STATICFILES_DIRS = (
    os.path.join(os.path.dirname(BASE_DIR), "static"),
)