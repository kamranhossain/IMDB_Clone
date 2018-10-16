from .base import *

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = env.str('DJANGO_SECRET_KEY', default='jkc_yb&5a2jn^1=2^i13#kkr5rq45a@f@hmkfc&911xnos1o868u98')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = env.bool('DJANGO_DEBUG', default=True)

ALLOWED_HOSTS = [
    'localhost',
    '127.0.0.1',
]
