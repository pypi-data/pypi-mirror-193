import os

import django
from django.conf import settings


def orm():

    DJANGO_SETTINGS_MODULE = os.getenv('DJANGO_SETTINGS_MODULE')
    if not DJANGO_SETTINGS_MODULE:
        os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'settings')

    django.setup()

    if settings.DEBUG:
        print('DEBUG', settings.DEBUG)


if __name__ == '__main__':
    orm()
