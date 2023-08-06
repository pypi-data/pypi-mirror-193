# orm-django

The power of Django ORM for use in standalone scripts.

## Install

```
pip install orm-django
```

## Define Django settings

By default the ORM settings will use DJANGO_SETTINGS_MODULE from environment variable. If not found we will fallback to settings module.

## Minimum settings configuration

You should at least configure your INSTALLED_APPS in settings to be able to use its models:

```
INSTALLED_APPS = [
    'app_1',
    ...
    'app_n',
]
```

And the database:

```
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': DB_NAME,
        'USER': DB_USER,
        'PASSWORD': DB_PASSWORD,
        'HOST': DB_HOST
    },
}
```
