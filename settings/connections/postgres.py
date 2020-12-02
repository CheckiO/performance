import os
from decouple import config

# POSTGRES_HOST = config('POSTGRES_HOST', 'postgres')
# POSTGRES_PORT = config('POSTGRES_SERVICE_PORT', 5432, cast=int)
#
# POSTGRES_USERNAME = config('POSTGRES_USERNAME')
# POSTGRES_PASSWORD = config('POSTGRES_PASSWORD')
#
# POSTGRES_DATABASE_NAME = config('POSTGRES_DATABASE_NAME')

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

DATABASES = {
    # 'default': {
    #     'ENGINE': 'django.db.backends.postgresql',
    #     'NAME': POSTGRES_DATABASE_NAME,
    #     'USER': POSTGRES_USERNAME,
    #     'PASSWORD': POSTGRES_PASSWORD,
    #     'HOST': POSTGRES_HOST,
    #     'PORT': POSTGRES_PORT,
    # }
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

