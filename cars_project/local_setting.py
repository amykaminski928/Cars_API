
# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-y++i%le30m_a%r-t!udxwx0i_(&16p@-2j^v2u616!13^yhg92'


# Database
# https://docs.djangoproject.com/en/4.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'cars_database',
        'HOST': 'localhost',
        'USER': 'root',
        'PASSWORD': '0liver-El@1se'
    }
}
