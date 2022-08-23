from .base import *


STATICFILES_DIRS = (
    os.path.join(os.path.dirname(BASE_DIR), "static")
),


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'blogdb',
        'USER': 'root',
        'PASSWORD': 'Macfdlr4',
        'HOST': 'localhost',
        'PORT': '3306',
    }
}