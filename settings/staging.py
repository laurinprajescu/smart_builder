from base import *

DEBUG = False

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

STRIPE_PUBLISHABLE = os.getenv('STRIPE_PUBLISHABLE', 'pk_test_2FKvDfMFtVQSyYQ6jUbwVnm6')
STRIPE_SECRET = os.getenv('STRIPE_SECRET', 'sk_test_WisNyom7MSIM6MVcHdj3qP0z')

SITE_URL = 'https://smart-builder.herokuapp.com'
ALLOWED_HOSTS.append('smart-builder.herokuapp.com')
 
# Log DEBUG information to the console
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'handlers': {
        'console': {
            'class': 'logging.StreamHandler',
        },
    },
    'loggers': {
        'django': {
            'handlers': ['console'],
            'level': os.getenv('DJANGO_LOG_LEVEL', 'DEBUG'),
        },
    },
}