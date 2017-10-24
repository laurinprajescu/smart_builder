from base import *

DEBUG = True

INSTALLED_APPS.append('debug_toolbar')

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

STRIPE_PUBLISHABLE = os.getenv('STRIPE_PUBLISHABLE', 'pk_test_2FKvDfMFtVQSyYQ6jUbwVnm6')
STRIPE_SECRET = os.getenv('STRIPE_SECRET', 'sk_test_WisNyom7MSIM6MVcHdj3qP0z')