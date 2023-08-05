from .base import *
DEBUG = True

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []

# Database
# https://docs.djangoproject.com/en/4.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
#'NAME': 'dbuser', <- LO CAMBIO AL JSON QUE CONFIGURO EN MI PROYECTO CON DATOS SECRETOS, BD, USER Y CLAVE
        'NAME': get_secret('DB_NAME'),
        'USER': get_secret('USER'),
        'PASWORD': get_secret('PASSWORD'),
#       'USER': 'alfonso', <- CAMBIA POR SECRET
#       'PASSWORD': 'servi15', <- CAMBIA POR SECRET
        'HOST': 'localhost',
        'PORT': '5432',
    }
}
# Static Files (CSS, Javascript, Imágenes)
# Buscar documentación Django 

STATIC_URL = '/static/'
STATICFILES_DIRS = [BASE_DIR / 'static']

MEDIA_URL = '/media/'
# settings/local.py
from .base import *

DEBUG = True

# Configuración de archivos estáticos y media para desarrollo local
STATICFILES_DIRS = [BASE_DIR / 'static']
MEDIA_ROOT = BASE_DIR / 'media'