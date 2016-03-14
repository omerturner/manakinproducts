
# static is here manakinproducts_static
# using PostgreSQL -- manakinproducts
# username -- manakinproducts
# password -- OatK-100

from django.conf import settings

if not settings.DEBUG:

    import os

    BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))


    # Quick-start development settings - unsuitable for production
    # See https://docs.djangoproject.com/en/1.8/howto/deployment/checklist/

    # SECURITY WARNING: keep the secret key used in production secret!
    SECRET_KEY = 'q07008@^jv-&$s9zbiv2!$95g-mz#_p4h6wgvkvrn(osh^h_n+'

    # SECURITY WARNING: don't run with debug turned on in production!
    DEBUG = False

    ALLOWED_HOSTS = ['manakinproducts.com', 'www.manakinproducts.com']


    # Application definition

    INSTALLED_APPS = (
        'django.contrib.admin',
        'django.contrib.auth',
        'django.contrib.contenttypes',
        'django.contrib.sessions',
        'django.contrib.messages',
        'django.contrib.staticfiles',
        'django.contrib.humanize',
        'blog',
        'products',
        'contact',
        'seo',
    )

    MIDDLEWARE_CLASSES = (
        'django.contrib.sessions.middleware.SessionMiddleware',
        'django.middleware.common.CommonMiddleware',
        'django.middleware.csrf.CsrfViewMiddleware',
        'django.contrib.auth.middleware.AuthenticationMiddleware',
        'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
        'django.contrib.messages.middleware.MessageMiddleware',
        'django.middleware.clickjacking.XFrameOptionsMiddleware',
        'django.middleware.security.SecurityMiddleware',
    )

    ROOT_URLCONF = 'products_site.urls'

    TEMPLATES = [
        {
            'BACKEND': 'django.template.backends.django.DjangoTemplates',
            'DIRS': [os.path.join(BASE_DIR, 'templates')],
            'APP_DIRS': True,
            'OPTIONS': {
                'context_processors': [
                    'django.template.context_processors.debug',
                    'django.template.context_processors.request',
                    'django.core.context_processors.request',
                    "django.core.context_processors.i18n",
                    "django.core.context_processors.media",
                    "django.core.context_processors.static",
                    "django.core.context_processors.tz",
                    'django.contrib.auth.context_processors.auth',
                    'django.contrib.messages.context_processors.messages',
                    'seo.views.get_seos',
                ],
            },
        },
    ]

    WSGI_APPLICATION = 'products_site.wsgi.application'


    # Database
    # https://docs.djangoproject.com/en/1.8/ref/settings/#databases

    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.postgresql_psycopg2',
            'NAME': 'manakinproducts',
            'USER': 'manakinproducts',
            'PASSWORD': 'OatK-100',
        }
    }


    # Internationalization
    # https://docs.djangoproject.com/en/1.8/topics/i18n/

    LANGUAGE_CODE = 'en-us'

    TIME_ZONE = 'America/Los_Angeles'

    USE_I18N = True

    USE_L10N = True

    USE_TZ = True


    # Static files (CSS, JavaScript, Images)
    # https://docs.djangoproject.com/en/1.8/howto/static-files/

    STATIC_URL = '/static/'
    STATICFILES_DIRS = (
        os.path.join(BASE_DIR, 'assets'),
    )
    STATIC_ROOT = '/home/manakinp/webapps/manakin_products_static_cgi/'

    MEDIA_ROOT='/home/manakinp/webapps/manakin_products_media_cgi/'
    MEDIA_URL='/media/'


    EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
    EMAIL_HOST = 'smtp.webfaction.com'
    EMAIL_HOST_USER = 'manakin_support'
    EMAIL_HOST_PASSWORD = 'OatK-100'
    DEFAULT_FROM_EMAIL = 'support@manakinproducts.com'
    SERVER_EMAIL = 'support@manakinproducts.com'
